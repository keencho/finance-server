from fastapi import APIRouter, Response
from starlette.requests import Request

import schema
from core.decorators import auth
from core.constant import Constant
from service import account_service

account_router = APIRouter(prefix=f'{Constant.CONTEXT_PATH}/account/v1')


@account_router.post('/check-auth')
@auth
def check_auth(request: Request):
    return request.state.account


@account_router.post('/login')
def login(
        response: Response,
        login_schema: schema.LoginSchema = None,
):
    return account_service.login(schema=login_schema, response=response)


@account_router.post('/logout')
@auth
def logout(
        response: Response,
):
    return account_service.logout(response)
