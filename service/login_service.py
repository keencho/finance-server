from repository import account_repository
from sqlalchemy.orm import Session
from schema.login_schema import LoginSchema


def login(db: Session, login_schema: LoginSchema):
    account = account_repository.get_account_by_login_id(login_schema.login_id)