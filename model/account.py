import enum
import uuid

import peewee

from core.database import db


class AccountType(enum.Enum):
    ANONYMOUS = 'ANONYMOUS'
    USER = 'USER'
    ADMIN = 'ADMIN'


class Account(peewee.Model):
    id = peewee.CharField(unique=True, index=True, primary_key=True, default=uuid.uuid4)
    login_id = peewee.CharField(unique=True, null=False)
    name = peewee.CharField(null=False)
    password = peewee.CharField(null=False)
    upbit_access_key = peewee.CharField(null=True)
    upbit_private_key = peewee.CharField(null=True)
    telegram_token = peewee.CharField(null=True)
    telegram_chat_id = peewee.CharField(null=True)
    type = peewee.CharField(null=False)

    class Meta:
        database = db
        db_table = 'account'
