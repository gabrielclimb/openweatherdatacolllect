from pydantic import BaseModel
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
    sea_level: Optional[int]
    grnd_level: Optional[int]


class Wind(BaseModel):
    speed: float
    deg: int
    gust: Optional[float]


class Clouds(BaseModel):
    all: int


class Precipitation(BaseModel):
    h1: float = None
    h3: float = None

    class Config:
        fields = {"h1": "1h", "h3": "3h"}


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
    rain: Optional[Precipitation]
    snow: Optional[Precipitation]
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int
