from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from core.path import ContextPath, UpbitPath
from helper.upbit_helper import upbit_request
from repository import account_repository
from schema.account_schema import Account as AccountSchema

coin_router = APIRouter(
    prefix=f'{ContextPath.CONTEXT_PATH}/coin/v1'
)


@coin_router.get("/assets")
async def get_assets():
    return upbit_request(UpbitPath.ACCOUNT_INQUIRY)


@coin_router.get("/get", response_model=AccountSchema)
async def insert(db: Session = Depends(get_db)):
    account = account_repository.get_account_by_login_id(db, 'seyoung1231')
    return account

