from unittest.mock import Mock, patch

import pytest

from src.apis.api_handler import APIBaseClass


class MockAPI(APIBaseClass):
    def re_auth(self):
        self.session.headers.update({"Authorization": "Bearer newtoken"})


@pytest.fixture
def api_client():
    return MockAPI(base_url="https://testing.api")


@pytest.fixture
def mock_requests_get_current_weather():
    with patch("requests.Session.get") as mock_get:
        weather_data = {
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
            "timezone": 3600,
            "id": 2740952,
            "name": "Cavaco",
            "cod": 200,
        }
        mock_get.return_value = Mock(
            status_code=200,
            json=Mock(return_value=weather_data),
        )
        yield mock_get
