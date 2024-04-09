from src.helpers.api_handler import APIBaseClass


class OpenWeather(APIBaseClass):

    def re_auth(self): ...

    def __init__(self, base_url: str): ...
