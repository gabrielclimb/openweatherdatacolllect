from sqlmodel import Session, select
from typing import Optional
from src.db import engine
from src.db.models import Cities


def get_all_cities(session: Optional[Session] = None):
    if session is None:
        with Session(engine) as session:
            return _get_all_cities(session)
    else:
        return _get_all_cities(session)


def _get_all_cities(session: Session):
    statement = select(Cities)
    results = session.exec(statement).all()
    return results


if __name__ == "__main__":
    all = get_all_cities()
    print(all)
