import uuid

import jwt
import requests

from core.config import Config
from core.path import UpbitPath
from exception.exception import FinanceCommonException

BASE_URL = UpbitPath.BASE_URL


def upbit_request(path: str):
    res = requests.get(BASE_URL + path, headers=_get_headers())

    if res.status_code != 200:
        raise FinanceCommonException('upbit 요청 실패 - ' + path)

    return res.json()


def _get_headers():
    payload = {
            'access_key': Config.UPBIT_ACCESS_KEY,
            'nonce': str(uuid.uuid4())
    }

    jwt_token = jwt.encode(payload, Config.UPBIT_SECRET_KEY)
    authorize_token = 'Bearer {}'.format(jwt_token)

    return {"Authorization": authorize_token}