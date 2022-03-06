from urllib.request import Request

from fastapi import FastAPI
from starlette.responses import JSONResponse

from core.path import UpbitPath
from exception.upbit_request_failure import UpbitRequestFailureException
from helper.upbit_helper import upbit_request
from api.upbit import upbit_router

# swagger 비활성화
app = FastAPI(openapi_url=None)

app.include_router(upbit_router)


@app.exception_handler(UpbitRequestFailureException)
async def common_exception_handler(request: Request, exc: UpbitRequestFailureException):
    return JSONResponse(
        status_code=400,
        content={
            'success': False,
            'type': 'UPBIT_REQUEST_FAILURE',
            'message' : f'{exc}'
        },
    )

