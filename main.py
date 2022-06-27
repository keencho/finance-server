import datetime

import peewee
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

import core
import schema
import util
from api.account import account_router
from core import database
from core.config import Config
from core.request_middleware import RequestMiddleware
from model import AccountType
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

app.add_middleware(RequestMiddleware)


# post construct
@app.on_event('startup')
async def startup_event():
    super_admin_account = account_repository.get_by_login_id(Config.SUPER_ADMIN_ID)

    if super_admin_account is None:
        account_service.create_account(
            AccountCreateSchema(
                login_id=Config.SUPER_ADMIN_ID,
                password=Config.SUPER_ADMIN_PW,
                name=Config.SUPER_ADMIN_NAME,
                type=AccountType.ADMIN
            )
        )


# 미들웨어 처리 -> 모든 요청과 응답을 컨트롤한다.
@app.middleware("http")
async def middleware_handler(request: Request, call_next):
    try:
        # 요청 시작 전에 request.state.account에 jwt token을 파싱한 account 객체를 담는다.
        jwt_token_account = None
        cookies = request.cookies
        if cookies is not None:
            jwt_token = cookies.get(core.Config.JWT_COOKIE_NAME)
            if jwt_token is not None:
                try:
                    token = util.decode_access_token(token=jwt_token)
                    jwt_token_account = schema.JwtTokenAccountSchema.parse_obj(token)
                except:
                    pass

        request.state.account = jwt_token_account
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


