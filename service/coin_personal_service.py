import pprint

import core
import pyupbit

default_ticker="KRW-BTC"

access_key = core.Config.UPBIT_ACCESS_KEY
secret_key = core.Config.UPBIT_SECRET_KEY

upbit = pyupbit.Upbit(access=access_key, secret=secret_key)


# 전체 계좌 잔액 조회
def get_all_balance():
    return upbit.get_balances()


# 특정 계좌 잔액 조회
def get_balance(ticker=default_ticker):
    return upbit.get_balance(ticker)


# 지정가 매수
def buy():
    upbit.buy_limit_order()


if __name__ == '__main__':
    balance= upbit.get_balances()
    pprint.pprint(balance)