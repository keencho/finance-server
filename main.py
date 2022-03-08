import json
from urllib.request import Request

from fastapi import FastAPI
from starlette.responses import JSONResponse, Response

from api.account import account_router
from api.coin import coin_router
from core.container import Container
from exception.exception import FinanceCommonException

container = Container()

db = container.db()
db.create_database()

# swagger 비활성화
app = FastAPI(openapi_url=None)
app.include_router(coin_router)
app.include_router(account_router)


@app.middleware("http")
async def access_db_middleware(request: Request, call_next):
    try:
        response = await call_next(request)

        body = b""
        async for chunk in response.body_iterator:
            if chunk != b'null':
                body += chunk

        # 1. byte to str
        response_body: str = body.decode('utf-8')

        # 2. check if response_body is json format
        try:
            response_body = json.loads(response_body)
        except json.JSONDecodeError:
            # 'response body ' was not as json format
            print('not json format')

        return JSONResponse(
            content={
                'success:': True,
                'data': response_body
            },
            status_code=200,
        )
    except FinanceCommonException as e:
        return JSONResponse(
            status_code=200,
            content={
                'success': False,
                'message' : f'{e}'
            },
        )
    except Exception:
        return JSONResponse(
            status_code=200,
            content={
                'success': False,
                'message' : '알수없는 에러가 발생했습니다.'
            },
        )
