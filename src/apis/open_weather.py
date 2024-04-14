from typing import Optional
from src.helpers.api_handler import APIBaseClass


class OpenWeather(APIBaseClass):
    base_url = "https://openweathermap.org"

    def re_auth(self): ...

    def __init__(self, base_url: Optional[str] = None) -> None:
        self.base_url = base_url if base_url else self.base_url
