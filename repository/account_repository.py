from sqlalchemy.orm import Session

from model.account import Account
from schema.account_schema import AccountCreateBase
from util.password_util import encrypt_password


def create(db: Session, account_create_base: AccountCreateBase) -> Account:
    account = Account(
        login_id=account_create_base.login_id,
        password=encrypt_password(account_create_base.password),
        upbit_access_key=account_create_base.upbit_access_key,
        upbit_private_key=account_create_base.upbit_private_key
    )
    db.add(account)
    db.commit()
    db.refresh(account)
    return account


def get_account_by_login_id(db: Session, login_id: str) -> Account | None:
    return db\
        .query(Account)\
        .filter(Account.login_id == login_id)\
        .first()