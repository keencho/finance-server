import pandas.core.series
import pyupbit

from core import Constant
from repository import ticker_repository
from schema import TickerBase
from service import system_data_service

default_ticker="KRW-BTC"


# 업비트 티커 조회
# verbose: True이면 한글이름, 영어이름까지 (json list)
#          False 이면 code만 (list)
def get_tickers(verbose: bool=True):
    return pyupbit.get_tickers(verbose=verbose)


# DB 티커 조회
def get_db_tickers(code, korean_name, english_name):
    return ticker_repository.search(code, korean_name, english_name)


# 업비트 티커 조회 후 db 티커 초기화 & 저장
def reset_coin_ticker():
    system_data_service.save_or_update_last_updated(Constant.SystemDataKey.COIN_MARKET_LAST_UPDATED_AT)

    ticker_repository.delete()
    tickers = get_tickers()

    for ticker in tickers:
        base = TickerBase(
            code=ticker['market'],
            korean_name=ticker['korean_name'],
            english_name=ticker['english_name']
        )
        ticker_repository.create(base)


# 업비트 티커 현재가 가져오기
def get_current_price(ticker=default_ticker, verbose=True):
    return pyupbit.get_current_price(ticker=ticker, verbose=verbose)


# 업비트 호가 정보
def get_orderbook(ticker=default_ticker):
    return pyupbit.get_orderbook(ticker)


# 업비트 과거 시세 가져오기
def get_ohlcv(ticker=default_ticker):
    ohlcv = pyupbit.get_ohlcv(ticker)
    return ohlcv['close']


# 이동평균 구하기
def get_moving_average(series: pandas.core.series.Series, day=5):
    ma5 = series.rolling(day).mean()
    return ma5[-2]


# 상승장 여부
def is_bull_market(ticker=default_ticker):
    target = get_moving_average(get_ohlcv(ticker))
    current_price = get_current_price(ticker, verbose=False)
    return current_price > target


if __name__ == "__main__":
    reset_coin_ticker()