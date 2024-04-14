from pydantic import BaseModel, Field
from typing import List, Optional


class Coord(BaseModel):
    lon: float
    lat: float


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: Optional[int] = None
    grnd_level: Optional[int] = None


class Wind(BaseModel):
    speed: float
    deg: int
    gust: Optional[float] = None


class Clouds(BaseModel):
    all: int


class Precipitation(BaseModel):
    h1: float = Field(None, alias="1h")
    h3: float = Field(None, alias="3h")


class Sys(BaseModel):
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int


class WeatherData(BaseModel):
    coord: Coord
    weather: List[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    clouds: Clouds
    rain: Optional[Precipitation] = None
    snow: Optional[Precipitation] = None
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int
