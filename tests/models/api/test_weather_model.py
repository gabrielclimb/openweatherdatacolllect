import pytest
from pydantic import ValidationError

from src.models.api import WeatherData


def test_weather_data_model():
    full_json = {
        "coord": {"lon": -8.6167, "lat": 41.15},
        "weather": [
            {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}
        ],
        "base": "stations",
        "main": {
            "temp": 23.98,
            "feels_like": 24.05,
            "temp_min": 22.75,
            "temp_max": 29.74,
            "pressure": 1022,
            "humidity": 62,
        },
        "visibility": 10000,
        "wind": {"speed": 3.13, "deg": 280, "gust": 3.13},
        "clouds": {"all": 0},
        "dt": 1713105101,
        "sys": {
            "type": 2,
            "id": 2009460,
            "country": "PT",
            "sunrise": 1713074160,
            "sunset": 1713121972,
        },
        "rain": {"1h": 3.16},
        "snow": {"3h": 6.00},
        "timezone": 3600,
        "id": 2740952,
        "name": "Testing",
        "cod": 200,
    }

    weather = WeatherData(**full_json)

    assert weather.snow.h3 == 6
    assert weather.rain.h1 == 3.16
    assert weather.name == "Testing"


def test_fail_parse_weather_data_model():
    full_json = {
        "base": "stations",
        "main": {
            "temp": 23.98,
            "feels_like": 24.05,
            "temp_min": 22.75,
            "temp_max": 29.74,
            "pressure": 1022,
            "humidity": 62,
        },
        "visibility": 10000,
        "wind": {"speed": 3.13, "deg": 280, "gust": 3.13},
        "clouds": {"all": 0},
        "dt": 1713105101,
        "sys": {
            "type": 2,
            "id": 2009460,
            "country": "PT",
            "sunrise": 1713074160,
            "sunset": 1713121972,
        },
        "rain": {"1h": 3.16},
        "snow": {"3h": 6.00},
        "timezone": 3600,
        "id": 2740952,
        "name": "Testing",
        "cod": 200,
    }

    with pytest.raises(ValidationError):
        _ = WeatherData(**full_json)
