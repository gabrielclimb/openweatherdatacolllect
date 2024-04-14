from typing import Optional
from src.helpers.api_handler import APIBaseClass


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

    def get_weather_by_coords(
        self, latitude: float, longitude: float, units: str = "metric"
    ):
        url_current_weather = "data/2.5/weather"
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": self.api_key,
            "units": units,
        }
        _ = self.get(url_current_weather, params=params)

        return self.get(url_current_weather, params=params)


api = OpenWeather(api_key="c2178e2c834d1048fffceb856ffae7bb")
asn = api.get_weather_by_coords(latitude=41.150, longitude=-8.6166668)
print(asn)
