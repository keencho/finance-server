from fastapi import APIRouter
from core.path import ContextPath, UpbitPath
from helper.upbit_helper import upbit_request

upbit_router = APIRouter(
    prefix=f'{ContextPath.CONTEXT_PATH}/api/v1/upbit'
)


@upbit_router.get("/assets")
async def get_assets():
    return upbit_request(UpbitPath.ACCOUNT_INQUIRY)

