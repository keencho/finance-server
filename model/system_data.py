import peewee
from core.database import db


class SystemData(peewee.Model):
    key = peewee.CharField(unique=True, index=True)
    value = peewee.CharField()

    class Meta:
        database = db
        db_table = 'system_data'
