import pandas as pd
from sqlalchemy import create_engine, orm

import schema
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


def bull_market():
    with pd.option_context(
            'display.max_rows', None,
            'display.max_columns', None,
            'display.width', None):
        print(get_ohlcv("KRW-BTC"))


if __name__ == '__main__':
    bull_market()