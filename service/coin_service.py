import pprint

import pyupbit

from core import Constant
from repository import ticker_repository
from schema import TickerCreateBase
from service import system_data_service


# 업비트 티커 조회
# verbose: True이면 한글이름, 영어이름까지 (json list)
#          False 이면 code만 (list)
def get_tickers(verbose: bool=True):
    return pyupbit.get_tickers(verbose=verbose)


# 업비트 티커 조회 후 db 티커 초기화 & 저장
def reset_coin_ticker():
    system_data_service.save_or_update_last_updated(Constant.SystemDataKey.COIN_MARKET_LAST_UPDATED_AT)

    ticker_repository.delete()
    tickers = get_tickers()

    for ticker in tickers:
        base = TickerCreateBase(
            code=ticker['market'],
            korean_name=ticker['korean_name'],
            english_name=ticker['english_name']
        )
        ticker_repository.create(base)


# 업비트 티커 현재가 가져오기
def get_current_price(ticker="KRW-BTC", verbose=True):
    return pyupbit.get_current_price(ticker=ticker, verbose=verbose)


# 업비트 호가 정보
def get_orderbook(ticker="KRW-BTC"):
    i = pyupbit.get_orderbook(ticker)
    pprint.pprint(i)


if __name__ == '__main__':
    tickers = get_tickers()
    tickers = tickers[0:10]
    get_orderbook(tickers)
