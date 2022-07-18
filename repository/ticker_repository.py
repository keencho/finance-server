from functools import reduce

from model import Ticker
from schema import TickerBase
import operator

from util.peewee_util import and_

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


def search(code, korean_name, english_name):
    clauses = []
    if code:
        clauses.append(model.code.contains(code))
    if korean_name:
        clauses.append(model.korean_name.contains(korean_name))
    if english_name:
        clauses.append(model.english_name.contains(english_name))

    return list(model.select().where(and_(clauses)).dicts())