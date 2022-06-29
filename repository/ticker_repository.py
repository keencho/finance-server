from model import Ticker
from schema import TickerCreateBase

model = Ticker


def create(schema: TickerCreateBase):
    market = model(
        code=schema.code,
        korean_name=schema.korean_name,
        english_name=schema.english_name
    )

    market.save(force_insert=True)

    return market


def delete():
    model.delete().execute()