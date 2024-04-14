from src.db.models import City
from src.db.operations import get_all_cities, load_cities_from_yaml


def test_get_all_cities(session):
    city1 = City(
        name="CityOne",
        country="CountryOne",
        latitude=34.05,
        longitude=-118.25,
    )
    city2 = City(name="CityTwo", country="CountryTwo", latitude=40.71, longitude=-74.01)
    session.add(city1)
    session.add(city2)
    session.commit()

    cities = get_all_cities(session)

    assert len(cities) == 2
    assert cities[0].name == "CityOne"
    assert cities[1].name == "CityTwo"


def test_load_cities_from_yaml(session):
    load_cities_from_yaml(session)

    result = get_all_cities(session)

    assert len(result) == 4
