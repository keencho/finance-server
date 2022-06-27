from fastapi import APIRouter, Response
from starlette.requests import Request

import schema
from core.decorators import auth
from core.path import ContextPath
from service import account_service

account_router = APIRouter(prefix=f'{ContextPath.CONTEXT_PATH}/account/v1')


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
async def logout(
        response: Response,
):
    return account_service.logout(response)