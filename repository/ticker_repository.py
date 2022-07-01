from model import Ticker
from schema import TickerBase

model = Ticker


def create(schema: TickerBase):
    market = model(
        code=schema.code,
        korean_name=schema.korean_name,
        english_name=schema.english_name
    )

    market.save(force_insert=True)

    return market


def delete():
    model.delete().execute()


def list_all():
    return list(model.select().execute())