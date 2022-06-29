import datetime


def get_date(format: str='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.today().strftime(format)