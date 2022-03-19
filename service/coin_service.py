import pandas as pd
from sqlalchemy import create_engine, orm

import helper
import schema
import util
from core.database import Base
from helper.upbit_helper import *
from repository.market_repository import MarketRepository

engine = create_engine(core.Config.DB_FULL_URL)
Base.metadata.create_all(engine)
session_factory = orm.scoped_session(
    orm.sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
market_repository = MarketRepository(session_factory=session_factory)


def create_market():
    for row in get_market_code():
        exist_row = market_repository.get_market_by_code(row['market'])
        if exist_row is not None:
            continue
        base = schema.MarketCreateBase(
            code=row['market'],
            korean_name=row['korean_name'],
            english_name=row['english_name']
        )
        market_repository.create(base)


def is_bull_market(ticker: str):
    """
    상승장 여부 확인
    """
    moving_average_window = 5

    with util.pandas_beauty_print():
        ohlcv = get_ohlcv(ticker)

        close_price = ohlcv['close']
        # -1: 오늘, -2: 어제
        last_ma5 = close_price.rolling(moving_average_window).mean()[-2]
        price = helper.get_current_price(ticker)

        return price > last_ma5


if __name__ == '__main__':
    t = is_bull_market(ticker="KRW-ETH")
