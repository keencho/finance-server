import json
from urllib.request import Request

from fastapi import FastAPI
from starlette.authentication import AuthenticationBackend, AuthCredentials, SimpleUser
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import JSONResponse

from api.account import account_router
from api.coin import coin_router
from core.config import Config
from core.container import Container
from exception.exception import FinanceCommonException, FinanceNotFoundException, FinanceUnAuthorizedException
from schema.account_schema import JwtTokenAccount
from util.jwt_util import decode_access_token

container = Container()

db = container.db()
db.create_database()

# swagger 비활성화
app = FastAPI(openapi_url=None)
app.include_router(coin_router)
app.include_router(account_router)


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        cookies = conn.cookies
        jwt_token = cookies.get(Config.JWT_COOKIE_NAME)

        jwt_token_account = None
        if jwt_token is not None:
            token = decode_access_token(token=jwt_token)
            jwt_token_account = JwtTokenAccount.parse_obj(token)

        conn.state.current_account = jwt_token_account

        if jwt_token_account is None:
            return AuthCredentials(['not-authenticated']), SimpleUser('Anonymous')
        else:
            return AuthCredentials(['authenticated']), SimpleUser(jwt_token_account.login_id)


app.add_middleware(AuthenticationMiddleware, backend=BasicAuthBackend())


@app.middleware("http")
async def middelware_handler(request: Request, call_next):
    try:
        response = await call_next(request)

        if response.status_code == 403:
            raise FinanceUnAuthorizedException()

        if response.status_code == 404:
            raise FinanceNotFoundException()

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
            # 'response body ' is not json format
            print('not json format')

        return JSONResponse(
            content=response_body,
            headers=dict(response.headers),
            status_code=200
        )
    except FinanceCommonException as e:
        return JSONResponse(
            status_code=200,
            content={
                'success': False,
                'message' : f'{e}'
            },
        )
    except FinanceUnAuthorizedException as e:
        return JSONResponse(
            status_code=403,
            content={
                'success': False,
                'message' : f'{e}'
            },
        )
    except FinanceNotFoundException as e:
        return JSONResponse(
            status_code=404,
            content={
                'success': False,
                'message': f'{e}'
            }
        )
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=200,
            content={
                'success': False,
                'message' : '알수없는 에러가 발생했습니다.'
            },
        )
