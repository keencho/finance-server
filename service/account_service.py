from fastapi import Response

import core
import schema
import util
from core.exception import NotFoundException, UnAuthorizedException, CommonException
from repository import account_repository


def login(schema: schema.LoginSchema, response: Response):
    account = account_repository.get_by_login_id(schema.login_id)

    if account is None:
        raise NotFoundException('존재하는 계정이 없습니다.')

    if not util.check_password(account.password, schema.password):
        raise UnAuthorizedException('비밀번호가 일치하지 않습니다.')

    access_token = util.create_access_token(account=account)

    response.set_cookie(key=core.Config.JWT_COOKIE_NAME, value=access_token)

    return access_token


def create_account(schema: schema.AccountCreateSchema):
    account = account_repository.get_by_login_id(schema.login_id)

    if account is not None:
        raise CommonException('이미 사용중이거나 탈퇴한 아이디입니다.')

    return account_repository.create(schema)


def logout(response: Response):
    response.set_cookie(key=core.Config.JWT_COOKIE_NAME, value='')

    return None
