from typing import Optional

import yaml
from sqlmodel import Session, select

from src.db import engine
from src.db.models import City


def get_all_cities(session: Optional[Session] = None):
    if session is None:
        with Session(engine) as session:
            return _get_all_cities(session)
    else:
        return _get_all_cities(session)


def _get_all_cities(session: Session) -> list[City]:
    statement = select(City)
    results = session.exec(statement).all()
    return results


def load_cities_from_yaml(session: Optional[Session] = None) -> None:
    with open("cities.yaml", "r") as f:
        cities_data = yaml.safe_load(f)["Cities"]

    for city_name, city_details in cities_data.items():
        city = City(
            name=city_name,
            country=city_details["Country"],
            latitude=city_details["lat"],
            longitude=city_details["long"],
        )
        session.add(city)
    session.commit()


if __name__ == "__main__":
    all = get_all_cities()
    print(all)
