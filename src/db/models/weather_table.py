from typing import Optional

from sqlmodel import Field, SQLModel


class Cities(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    city_name: str
    country_name: str
    latitude: float
    longitude: float
