from fastapi import Response

import core
import schema
import util
from exception.exception import FinanceCommonException
from repository.account_repository import AccountRepository


class AccountService:
    def __init__(
            self,
            account_repository: AccountRepository
    ) -> None:
        self._account_repository: AccountRepository = account_repository

    def login(self, login_schema: schema.LoginSchema, response: Response):
        account = self._account_repository.get_account_by_login_id(login_schema.login_id)

        if account is None:
            raise FinanceCommonException('존재하는 계정이 없습니다.')

        if not util.check_password(account.password, login_schema.password):
            raise FinanceCommonException('비밀번호가 일치하지 않습니다.')

        access_token = util.create_access_token(account=account)

        response.set_cookie(key=core.Config.JWT_COOKIE_NAME, value=access_token)

        return access_token

    def logout(self, response: Response):
        response.set_cookie(key=core.Config.JWT_COOKIE_NAME, value='')
        return None
