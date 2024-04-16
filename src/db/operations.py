from typing import Optional

import yaml
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from src.db import engine
from src.db.models import City


def get_all_cities(session: Optional[Session] = None) -> list[City]:
    """
    Retrieve all cities from the database.

    Args:
        session (Optional[Session]): The database session. If not provided, a new session will be created.

    Returns:
        list[City]: A list of City objects representing all the cities in the database.
    """
    if session is None:
        with Session(engine) as session:
            return _get_all_cities(session)
    else:
        return _get_all_cities(session)


def _get_all_cities(session: Session) -> list[City]:
    """
    Helper function to retrieve all cities from the database.

    Args:
        session (Session): The database session.

    Returns:
        list[City]: A list of City objects representing all the cities in the database.
    """
    statement = select(City)
    results = session.exec(statement).all()
    return results


def load_cities_from_yaml(session: Optional[Session] = None) -> None:
    """
    Load cities from a YAML file and add them to the database.

    Args:
        session (Optional[Session]): The database session. If not provided, a new session will be created.

    Returns:
        None
    """
    with open("cities.yaml", "r") as f:
        cities_data = yaml.safe_load(f)["Cities"]

    if session is None:
        with Session(engine) as session:
            _load_cities_from_yaml(cities_data, session)
    else:
        _load_cities_from_yaml(cities_data, session)


def _load_cities_from_yaml(cities_data: dict, session: Session) -> list[City]:
    """
    Helper function to add cities to the database.

    Args:
        cities_data (dict): A dictionary containing city data.
        session (Session): The database session.

    Returns:
        list[City]: A list of City objects representing the cities that were added to the database.
    """
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
