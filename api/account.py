from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Response
from starlette.authentication import requires
from starlette.requests import Request

from core.container import Container
from core.path import ContextPath
from repository.account_repository import AccountRepository
from schema.account_schema import LoginSchema
from service.account_service import AccountService
from util.response_util import build_success_response

account_router = APIRouter(prefix=f'{ContextPath.CONTEXT_PATH}/account/v1')


@account_router.post('/login')
@inject
async def login(
        request: Request,
        response: Response,
        login_schema: LoginSchema = None,
        account_service: AccountService = Depends(Provide[Container.account_service]),
):
    return build_success_response(account_service.login(login_schema=login_schema, response=response))


@account_router.get('/check-duplicate')
@inject
async def check_duplicate(
        login_id: str = None,
        account_repository: AccountRepository = Depends(Provide[Container.account_repository])
) -> bool:
    if login_id is None or len(login_id) == 0:
        return False

    return account_repository.get_account_by_login_id(login_id) is None