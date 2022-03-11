from fastapi import Response

from core.config import Config
from exception.exception import FinanceCommonException
from repository.account_repository import AccountRepository
from schema.account_schema import LoginSchema, JwtTokenAccount, AccountCreateBase
from util.jwt_util import create_access_token
from util.password_util import check_password


class AccountService:
    def __init__(
            self,
            account_repository: AccountRepository
    ) -> None:
        self._account_repository: AccountRepository = account_repository

    def login(self, login_schema: LoginSchema, response: Response):
        account = self._account_repository.get_account_by_login_id(login_schema.login_id)

        if account is None:
            raise FinanceCommonException('존재하는 계정이 없습니다.')

        if not check_password(account.password, login_schema.password):
            raise FinanceCommonException('비밀번호가 일치하지 않습니다.')

        access_token = create_access_token(account=account)

        response.set_cookie(key=Config.JWT_COOKIE_NAME, value=access_token)

        return access_token

    def logout(self, response: Response):
        response.set_cookie(key=Config.JWT_COOKIE_NAME, value='')
        return None
