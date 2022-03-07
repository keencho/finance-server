from urllib.request import Request

from fastapi import FastAPI
from starlette.responses import JSONResponse

from api.account import account_router
from api.coin import coin_router
from core.container import Container
from exception.upbit_request_failure import UpbitRequestFailureException


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    # swagger 비활성화
    app = FastAPI(openapi_url=None)
    app.include_router(coin_router)
    app.include_router(account_router)

    return app


app = create_app()


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
