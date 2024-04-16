from abc import ABC, abstractmethod
from os.path import join

import requests
from requests.adapters import HTTPAdapter, Retry

from src.helpers.errors import BadRequestError, NotFoundError, TooManyRequestsError


class APIBaseClass(ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        session = requests.Session()
        retries = Retry(total=5, backoff_factor=2, status_forcelist=[502, 503, 504])
        session.mount("https://", HTTPAdapter(max_retries=retries))
        return session

    @abstractmethod
    def re_auth(self):
        pass

    def _request(self, method, url, *args, **kwargs):
        full_url = join(self.base_url, url)
        response = getattr(self.session, method)(full_url, *args, **kwargs)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                self.re_auth()
                response = getattr(self.session, method)(full_url, *args, **kwargs)
            elif response.status_code == 400:
                raise BadRequestError()
            elif response.status_code == 404:
                raise NotFoundError()
            elif response.status_code == 429:
                raise TooManyRequestsError()
            else:
                raise e

        return response

    def post(self, url, *args, **kwargs):
        return self._request("post", url, *args, **kwargs)

    def get(self, url, *args, **kwargs):
        return self._request("get", url, *args, **kwargs)
