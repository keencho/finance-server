import util
from model.account import Account
from schema.account_schema import AccountCreateSchema

model = Account


def get(id: str):
    return model.filter(model.id == id).first()


def get_by_login_id(login_id: str):
    return model.filter(model.login_id == login_id).first()


def create(account_schema: AccountCreateSchema):
    account = Account(
        login_id=account_schema.login_id,
        password=util.encrypt_password(account_schema.password),
        name=account_schema.name
    )
    account.save(force_insert=True)

    return account

