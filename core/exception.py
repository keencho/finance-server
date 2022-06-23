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
        self.status_code = 401
        self.error = 'Not Found Error'

    def __str__(self):
        return self.value


class UnAuthorizedException(Exception):
    def __init__(self, value):
        self.value = value
        self.status_code = 401
        self.error = 'Unauthorized Error'

    def __str__(self):
        return self.value
