from typing import Optional

from sqlmodel import Field, SQLModel
from src.apis.models import Coord


class Cities(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    city_name: str
    country_name: str
    coord: Coord
