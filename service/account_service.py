from exception.exception import FinanceCommonException
from repository.account_repository import AccountRepository
from schema.account_schema import LoginSchema, JwtTokenAccount
from service.jwt_service import JwtService
from util.password_util import check_password


class AccountService:
    def __init__(
            self,
            account_repository: AccountRepository,
            jwt_service: JwtService
    ) -> None:
        self._account_repository: AccountRepository = account_repository
        self._jwt_service: JwtService = jwt_service

    def login(self, login_schema: LoginSchema):
        account = self._account_repository.get_account_by_login_id(login_schema.login_id)

        if account is None:
            raise FinanceCommonException('존재하는 계정이 없습니다.')

        if not check_password(account.password, login_schema.password):
            raise FinanceCommonException('비밀번호가 일치하지 않습니다.')

        access_token = self._jwt_service.create_access_token(data=JwtTokenAccount.from_orm(account).dict())

        return access_token

