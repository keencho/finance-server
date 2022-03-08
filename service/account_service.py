from exception.exception import FinanceCommonException
from repository.account_repository import AccountRepository
from schema.account_schema import LoginSchema


class AccountService:
    def __init__(self, account_repository: AccountRepository) -> None:
        self._account_repository: AccountRepository = account_repository

    def login(self, login_schema: LoginSchema):
        account = self._account_repository.get_account_by_login_id(login_schema.login_id)

        if account is None:
            raise FinanceCommonException('아이디 혹은 비밀번호가 일치하지 않습니다.')

        return {
            'nothing': 123
        }