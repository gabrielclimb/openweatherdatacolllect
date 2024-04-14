from typing import Optional

from src.apis.api_handler import APIBaseClass
from src.models.api import WeatherData, Coord


class OpenWeather(APIBaseClass):
    base_url = "https://api.openweathermap.org"

    def re_auth(self): ...

    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
    ) -> None:
        self.base_url = base_url if base_url else self.base_url
        super().__init__(self.base_url)
        self.api_key = api_key

    def get_weather_by_coords(self, coord: Coord, units: str = "metric") -> WeatherData:
        url_current_weather = "data/2.5/weather"

        params = {
            "lat": coord.lat,
            "lon": coord.lon,
            "appid": self.api_key,
            "units": units,
        }

        response = self.get(url_current_weather, params=params)

        return WeatherData(**response.json())


if __name__ == "__main__":
    from dotenv import load_dotenv
    import os

    load_dotenv()

    api_key = os.getenv("API_KEY")
    api = OpenWeather(api_key=api_key)
    ans = api.get_weather_by_coords(latitude=41.150, longitude=-8.6166668)
    print(ans)
