from fastapi import APIRouter

from core.constant import Constant
from service import coin_service

coin_router = APIRouter(prefix=f'{Constant.CONTEXT_PATH}/coin/v1')


# db 티커 조회
@coin_router.get('/tickers')
def get_tickers(code=None, korean_name=None, english_name=None):
    return coin_service.get_db_tickers(code, korean_name, english_name)


# db 티커 전체 리셋
@coin_router.put('/tickers')
def reset_tickers():
    pass