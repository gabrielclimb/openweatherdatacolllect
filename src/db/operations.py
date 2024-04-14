from typing import Optional

import yaml
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from src.db import engine
from src.db.models import City


def get_all_cities(session: Optional[Session] = None) -> list[City]:
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

    if session is None:
        with Session(engine) as session:
            _load_cities_from_yaml(cities_data, session)
    else:
        _load_cities_from_yaml(cities_data, session)


def _load_cities_from_yaml(cities_data: dict, session: Session) -> list[City]:
    for city_name, city_details in cities_data.items():
        city = City(
            name=city_name,
            country=city_details["Country"],
            latitude=city_details["lat"],
            longitude=city_details["long"],
        )
        try:
            session.add(city)
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f"City '{city_name}' already exists. Skipping...")


if __name__ == "__main__":
    load_cities_from_yaml()
