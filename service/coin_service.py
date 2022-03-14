from sqlalchemy import create_engine, orm

from core.database import Base
from helper.upbit_helper import *
from repository.market_repository import MarketRepository
from schema.market_schema import MarketCreateBase
from util.print_util import json_beauty_print

engine = create_engine(Config.DB_FULL_URL)
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
        base = MarketCreateBase(
            code=row['market'],
            korean_name=row['korean_name'],
            english_name=row['english_name']
        )
        market_repository.create(base)


def init():
    for row in get_orderbook(['KRW-BTC', 'KRW-ETH']):
        json_beauty_print(row)


if __name__ == '__main__':
    init()