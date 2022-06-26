import enum
import uuid

import peewee

from core.database import db


class Account(peewee.Model):
    id = peewee.CharField(unique=True, index=True, primary_key=True, default=uuid.uuid4)
    login_id = peewee.CharField(unique=True, null=False)
    name = peewee.CharField(null=False)
    password = peewee.CharField(null=False)
    upbit_access_key = peewee.CharField(null=True)
    upbit_private_key = peewee.CharField(null=True)
    telegram_token = peewee.CharField(null=True)
    telegram_chat_id = peewee.CharField(null=True)

    class Meta:
        database = db
        db_table = 'account'


class AccountType(enum.Enum):
    ANONYMOUS = 0
    USER = 1
    ADMIN = 2
