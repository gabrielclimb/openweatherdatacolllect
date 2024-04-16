from abc import ABC, abstractmethod
from os.path import join

import requests
from requests.adapters import HTTPAdapter, Retry

from src.helpers.errors import BadRequestError, NotFoundError, TooManyRequestsError


class APIBaseClass(ABC):
    """
    Base class for API handlers.

    Methods:
        re_auth(): Abstract method for re-authenticating the API.
        post(url, *args, **kwargs): Sends a POST request.
        get(url, *args, **kwargs): Sends a GET request.
    """

    def __init__(self, base_url: str) -> None:
        """
        Initializes an instance of APIBaseClass class.

        Args:
            base_url (str):  The base URL for the API.
        """
        self.base_url = base_url
        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        """
        Creates a session object with retry functionality.

        Returns:
            requests.Session: The session object.
        """
        session = requests.Session()
        retries = Retry(total=5, backoff_factor=2, status_forcelist=[502, 503, 504])
        session.mount("https://", HTTPAdapter(max_retries=retries))
        return session

    @abstractmethod
    def re_auth(self):
        """
        Abstract method for re-authenticating the API.
        """
        pass

    def _request(self, method, url, *args, **kwargs):
        """
        Sends an HTTP request and handles common errors.

        Args:
            method (str): The HTTP method (e.g., "get", "post").
            url (str): The URL for the request.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            requests.Response: The response object.

        Raises:
            BadRequestError: If the response status code is 400.
            NotFoundError: If the response status code is 404.
            TooManyRequestsError: If the response status code is 429.
            requests.exceptions.HTTPError: If the response status code is not handled.
        """
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
        """
        Sends a POST request.

        Args:
            url (str): The URL for the request.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            requests.Response: The response object.
        """
        return self._request("post", url, *args, **kwargs)

    def get(self, url, *args, **kwargs):
        """
        Sends a GET request.

        Args:
            url (str): The URL for the request.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            requests.Response: The response object.
        """
        return self._request("get", url, *args, **kwargs)
