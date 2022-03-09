from datetime import timedelta, datetime

from jose import jwt

from core.config import Config
from exception.exception import FinanceCommonException
from repository.account_repository import AccountRepository
from schema.account_schema import LoginSchema, Account
from util.password_util import check_password


class AccountService:
    def __init__(self, account_repository: AccountRepository) -> None:
        self._account_repository: AccountRepository = account_repository

    def login(self, login_schema: LoginSchema):
        account = self._account_repository.get_account_by_login_id(login_schema.login_id)

        if account is None:
            raise FinanceCommonException('존재하는 계정이 없습니다.')

        if not check_password(account.password, login_schema.password):
            raise FinanceCommonException('비밀번호가 일치하지 않습니다.')

        access_token = self.create_access_token(data={
            'hello': account.login_id
        })

        return access_token

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=int(Config.JWT_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, Config.JWT_SECRET_KEY, algorithm=Config.JWT_ALGORITHM)
        return encoded_jwt
