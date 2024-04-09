class UnauthorizedError(Exception):
    def __init__(
        self,
        message="Error 401 - Unauthorized. Authentication failed or was not provided.",
    ):
        super().__init__(message)


class BadRequestError(Exception):
    def __init__(
        self, message="Error 400 - Bad Request. The request is malformed or invalid."
    ):
        super().__init__(message)


class NotFoundError(Exception):
    def __init__(
        self, message="Error 404 - Not Found. The requested resource does not exist."
    ):
        super().__init__(message)


class TooManyRequestsError(Exception):
    def __init__(self, message="Error 429 - Too Many Requests. Rate limit exceeded."):
        super().__init__(message)
