import os

from dotenv import load_dotenv
from sqlmodel import Session

from src.apis.weather import OpenWeather
from src.db import engine
from src.db.models.tables import WeatherData
from src.db.operations import get_all_cities

load_dotenv()


API_KEY = os.getenv("API_KEY")


def ingest_weather_data() -> None:
    cities = get_all_cities()
    api_weather = OpenWeather(API_KEY)
    session = Session(engine)

    for city in cities:
        data = api_weather.get_weather_by_coords(city.latitude, city.longitude)
        w = WeatherData(
            city_id=city.id,
            lon=data.coord.longitude,
            lat=data.coord.latitude,
            weather_id=data.weather[0].id,
            weather_main=data.weather[0].main,
            weather_description=data.weather[0].description,
            weather_icon=data.weather[0].icon,
            base=data.base,
            temp=data.main.temp,
            feels_like=data.main.feels_like,
            temp_min=data.main.temp_min,
            temp_max=data.main.temp_max,
            pressure=data.main.pressure,
            humidity=data.main.humidity,
            sea_level=data.main.sea_level,
            grnd_level=data.main.grnd_level,
            visibility=data.visibility,
            wind_speed=data.wind.speed,
            wind_deg=data.wind.deg,
            wind_gust=data.wind.gust,
            rain_1h=data.rain.h1 if data.rain else None,
            rain_3h=data.rain.h3 if data.rain else None,
            snow_1h=data.snow.h1 if data.snow else None,
            snow_3h=data.snow.h3 if data.snow else None,
            clouds_all=data.clouds.all,
            dt=data.dt,
            sys_type=data.sys.type,
            sys_id=data.sys.id,
            sunrise=data.sys.sunrise,
            sunset=data.sys.sunset,
            timezone=data.timezone,
            cod=data.cod,
        )
        session.add(w)
        session.commit()
        print(f"Data for {city.name} ingested successfully.")

    session.close()


if __name__ == "__main__":
    ingest_weather_data()
