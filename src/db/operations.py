from sqlmodel import Session, select

from src.db import engine
from src.db.models import Cities


def get_all_cities():
    with Session(engine) as session:
        statement = select(Cities)
        results = session.exec(statement).all()
        return results


if __name__ == "__main__":
    all = get_all_cities()
    print(all)
