from src.apis.weather import OpenWeather
from src.apis.models import WeatherData


def test_open_weather_api(mock_requests_get_current_weather):
    open_weather_api = OpenWeather("dummy-key")
    response = open_weather_api.get_weather_by_coords(0, 1)

    assert isinstance(response, WeatherData)
    assert response.name == "Cavaco"
    assert response.rain is None
