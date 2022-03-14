from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from model.market import Market
from schema.market_schema import MarketCreateBase


class MarketRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_market_by_code(self, code: str) -> Market | None:
        with self.session_factory() as session:
            return session.query(Market).filter(Market.code == code).first()

    def create(self, base: MarketCreateBase):
        market = Market(
            code=base.code,
            korean_name=base.korean_name,
            english_name=base.english_name
        )

        with self.session_factory() as session:
            session.add(market)
            session.commit()
            session.refresh(market)
            return market
