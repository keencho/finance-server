from fastapi import APIRouter, Response
from starlette.requests import Request

import schema
from core.path import ContextPath
from service import account_service

account_router = APIRouter(prefix=f'{ContextPath.CONTEXT_PATH}/account/v1')


@account_router.get('/check-auth')
def check_auth(request: Request):
    return request.state.current_account


@account_router.post('/check-auth')
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


# @account_router.get('/check-duplicate')
# async def check_duplicate(
#         login_id: str = None,
#         account_repository: AccountRepository = Depends(Provide[Container.account_repository])
# ) -> bool:
#     if login_id is None or len(login_id) == 0:
#         return False
#
#     return account_repository.get_account_by_login_id(login_id) is None
