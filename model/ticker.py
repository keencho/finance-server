import peewee
from core.database import db


class Ticker(peewee.Model):
    code = peewee.CharField(primary_key=True, index=True, unique=True)
    korean_name = peewee.CharField()
    english_name = peewee.CharField()

    class Meta:
        database = db
        db_table = 'coin_ticker'
