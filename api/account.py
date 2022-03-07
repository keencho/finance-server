from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from core.path import ContextPath
from repository import account_repository
from schema.login_schema import LoginSchema
from service import login_service

account_router = APIRouter(
    prefix=f'{ContextPath.CONTEXT_PATH}/account/v1'
)


@account_router.post('/login')
async def login(db: Session = Depends(get_db), login_schema: LoginSchema = None):
    return login_service.login()


@account_router.get('/check-duplicate')
async def check_duplicate(db: Session = Depends(get_db), login_id: str = None) -> bool:
    account = account_repository.get_account_by_login_id(db, login_id)
    return account is None