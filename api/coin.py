from fastapi import APIRouter, Response
from starlette.requests import Request

import schema
from core.decorators import auth
from core.constant import Constant
from service import account_service
from service import coin_service


coin_router = APIRouter(prefix=f'{Constant.CONTEXT_PATH}/coin/v1')


@coin_router.get('/tickers')
def get_tickers():
    return coin_service.get_db_tickers()