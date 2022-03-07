from fastapi import APIRouter

from core.path import ContextPath, UpbitPath
from helper.upbit_helper import upbit_request

coin_router = APIRouter(
    prefix=f'{ContextPath.CONTEXT_PATH}/coin/v1'
)


@coin_router.get("/assets")
async def get_assets():
    return upbit_request(UpbitPath.ACCOUNT_INQUIRY)


