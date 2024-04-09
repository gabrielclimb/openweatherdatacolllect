import pytest

from src.helpers.api_handler import APIBaseClass


class MockAPI(APIBaseClass):
    def re_auth(self):
        self.session.headers.update({"Authorization": "Bearer newtoken"})


@pytest.fixture
def api_client():
    return MockAPI(base_url="https://testing.api")
