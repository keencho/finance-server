class FinanceCommonException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class FinanceNotFoundException(Exception):
    def __init__(self, value):
        self.value = value

    def __init__(self):
        self.value = 'Not Found'

    def __str__(self):
        return self.value


class FinanceUnAuthorizedException(Exception):
    def __init__(self, value):
        self.value = value

    def __init__(self):
        self.value = 'Forbidden'

    def __str__(self):
        return self.value
