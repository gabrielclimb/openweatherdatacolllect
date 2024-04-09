import pytest

from src.helpers.errors import BadRequestError


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code == 401:
            raise BadRequestError


def test_get_success(monkeypatch, api_client):
    def mock_get(*args, **kwargs):
        return MockResponse({"key": "value"}, 200)

    monkeypatch.setattr("requests.Session.get", mock_get)

    response = api_client.get("/data")
    assert response.json() == {"key": "value"}
    assert response.status_code == 200


def test_get_unauthorized(monkeypatch, api_client):
    def mock_get(*args, **kwargs):
        return MockResponse(None, 401)

    monkeypatch.setattr("requests.Session.get", mock_get)

    with pytest.raises(BadRequestError):
        _ = api_client.get("/data")
