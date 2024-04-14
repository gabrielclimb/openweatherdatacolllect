from src.db.models import Cities
from src.db.operations import get_all_cities


def test_get_all_cities(session):
    city1 = Cities(
        city_name="CityOne",
        country_name="CountryOne",
        latitude=34.05,
        longitude=-118.25,
    )
    city2 = Cities(
        city_name="CityTwo", country_name="CountryTwo", latitude=40.71, longitude=-74.01
    )
    session.add(city1)
    session.add(city2)
    session.commit()

    result = get_all_cities(session)

    assert len(result) == 2
    assert result[0].city_name == "CityOne"
    assert result[1].city_name == "CityTwo"
