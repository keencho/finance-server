import json

import pandas as pd


def json_beauty_print(json_data):
    print(json.dumps(json_data, indent=2))


def pandas_beauty_print():
    return pd.option_context(
        'display.max_rows', None,
        'display.max_columns', None,
        'display.width', None)
