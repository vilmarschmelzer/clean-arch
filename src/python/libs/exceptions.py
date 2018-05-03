class BaseException(Exception):
    def __init__(self, payload=None):
        self.payload = payload


class NotFound(BaseException):
    pass


class BadRequest(BaseException):
    pass
