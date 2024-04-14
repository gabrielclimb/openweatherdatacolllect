from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class City(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    country: str
    latitude: float
    longitude: float


class WeatherData(SQLModel, table=True):
    __tablename__ = "weather_data"
    id: Optional[int] = Field(default=None, primary_key=True)
    city_id: int
    lon: float
    lat: float
    weather_id: int
    weather_main: str
    weather_description: str
    weather_icon: str
    base: str
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: Optional[int] = None
    grnd_level: Optional[int] = None
    visibility: int
    wind_speed: float
    wind_deg: int
    wind_gust: Optional[float] = None
    rain_1h: Optional[float] = None
    rain_3h: Optional[float] = None
    snow_1h: Optional[float] = None
    snow_3h: Optional[float] = None
    clouds_all: int
    dt: int
    sys_type: int
    sys_id: int
    sys_message: Optional[str] = None
    sys_country: str
    sunrise: int
    sunset: int
    timezone: int
    cod: int
    created_at: Optional[datetime] = Field(
        default=None, sa_column_kwargs={"server_default": "CURRENT_TIMESTAMP"}
    )
