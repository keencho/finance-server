import datetime
from urllib.request import Request

import peewee
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from api.account import account_router
from core import database
from core.config import Config
from repository import account_repository
from service import account_service
from schema.account_schema import AccountCreateSchema

database.db.connect()
database.db.create_tables(peewee.Model.__subclasses__())
database.db.close()

# swagger 비활성화
app = FastAPI(openapi_url=None)
app.include_router(account_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# post construct
@app.on_event('startup')
async def startup_event():
    super_admin_account = account_repository.get_by_login_id(Config.SUPER_ADMIN_ID)

    if super_admin_account is None:
        account_service.create_account(
            AccountCreateSchema(
                login_id=Config.SUPER_ADMIN_ID,
                password=Config.SUPER_ADMIN_PW,
                name=Config.SUPER_ADMIN_NAME
            )
        )


# 미들웨어 처리 -> 모든 요청과 응답을 컨트롤한다.
@app.middleware("http")
async def middleware_handler(request: Request, call_next):
    try:
        response = await call_next(request)

        return response
    except Exception as e:
        if hasattr(e, 'status_code'):
            status_code = e.status_code
        else:
            status_code = 500

        if hasattr(e, 'error'):
            error = e.error
        else:
            error = 'Internal Server Error'

        return JSONResponse(
            status_code=status_code,
            content={
                'error': error,
                'message': e.__str__(),
                'path': request.url.path,
                'status': status_code,
                'timestamp': datetime.datetime.now().__str__()
            }
        )


