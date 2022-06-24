from functools import wraps

from fastapi import APIRouter, Response, Depends, Header
from starlette.requests import Request

import schema
from core.path import ContextPath
from service import account_service

account_router = APIRouter(prefix=f'{ContextPath.CONTEXT_PATH}/account/v1')


def check_header_api_key(param=None):
    def wrapper(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            print(param)
            # print(param)
            # print("%s %s" % (func.__name__, "before"))
            # print("%s %s" % (func.__name__ , "after"))
            return func(*args, **kwargs)
        return decorator
    return wrapper


@account_router.post('/check-auth')
@check_header_api_key
def check_auth(request: Request):
    return request.state.current_account


@account_router.post('/login')
def login(
        response: Response,
        login_schema: schema.LoginSchema = None,
):
    return account_service.login(schema=login_schema, response=response)


@account_router.post('/logout')
async def logout(
        response: Response,
):
    return account_service.logout(response)