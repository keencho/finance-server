class CommonException(Exception):
    def __init__(self, value):
        self.value = value
        self.status_code = 500
        self.error = 'Internal Server Error'

    def __str__(self):
        return self.value


class NotFoundException(Exception):
    def __init__(self, value):
        self.value = value
        self.status_code = 404
        self.error = 'Not Found Error'

    def __init__(self):
        self.value = 'Not Found'

    def __str__(self):
        return self.value


class UnAuthorizedException(Exception):
    def __init__(self, value):
        self.value = value
        self.status_code = 401
        self.error = 'Unauthorized Error'

    def __init__(self):
        self.value = 'Forbidden'

    def __str__(self):
        return self.value


def get_status_code(exception: Exception):
    if isinstance(exception, CommonException):
        return 500
    if isinstance(exception, NotFoundException):
        return 404
    if isinstance(exception, UnAuthorizedException):
        return 401

    return 500
