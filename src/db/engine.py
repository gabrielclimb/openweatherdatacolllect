from sqlmodel import Session, select

from src.db.engine import engine
from src.models.db import Cities


def get_all_records():
    with Session(engine) as session:
        statement = select(Cities)
        results = session.exec(statement).all()
        return results


if __name__ == "__main__":
    all = get_all_records()
    print(all)
