from src.apis.weather import OpenWeather
from src.models.api import WeatherData, Coord


def test_open_weather_api(mock_requests_get_current_weather):
    open_weather_api = OpenWeather("dummy-key")
    coord = Coord(lat=1.0, lon=0.0)
    response = open_weather_api.get_weather_by_coords(coord)

    assert isinstance(response, WeatherData)
    assert response.name == "Cavaco"
    assert response.rain is None
