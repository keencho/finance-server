from repository import system_data_repository
from util.date_time_util import get_date


def save_or_update_last_updated(key: str):
    system_data_repository.save_or_update(key, get_date())