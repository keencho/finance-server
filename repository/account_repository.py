from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from model.account import Account
from schema.account_schema import AccountCreateBase
from util.password_util import encrypt_password


class AccountRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_account_by_login_id(self, login_id: str) -> Account | None:
        with self.session_factory() as session:
            return session.query(Account).filter(Account.login_id == login_id).first()

    def create(self, account_create_base: AccountCreateBase) -> Account:
        account = Account(
            login_id=account_create_base.login_id,
            password=encrypt_password(account_create_base.password),
            upbit_access_key=account_create_base.upbit_access_key,
            upbit_private_key=account_create_base.upbit_private_key
        )
        with self.session_factory() as session:
            session.add(account)
            session.commit()
            session.refresh(account)
            return account


