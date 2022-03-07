from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from core.container import Container
from core.path import ContextPath
from repository.account_repository import AccountRepository
from schema.login_schema import LoginSchema
from service import login_service

account_router = APIRouter(prefix=f'{ContextPath.CONTEXT_PATH}/account/v1')


@account_router.post('/login')
@inject
async def login(login_schema: LoginSchema = None):
    return login_service.login()


@account_router.get('/check-duplicate')
@inject
async def check_duplicate(
        login_id: str = None,
        account_repository: AccountRepository = Depends(Provide[Container.account_repository])
) -> bool:
    if login_id is None or len(login_id) == 0:
        return False

    return account_repository.get_account_by_login_id(login_id) is None