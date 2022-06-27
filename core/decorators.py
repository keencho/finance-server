from functools import wraps

import core
import schema
import util
from core.exception import UnAuthorizedException
from model import AccountType


def doublewrap(f):
    '''
    a decorator decorator, allowing the decorator to be used as:
    @decorator(with, arguments, and=kwargs)
    or
    @decorator
    '''
    @wraps(f)
    def new_dec(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            # actual decorated function
            return f(args[0])
        else:
            # decorator arguments
            return lambda realf: f(realf, *args, **kwargs)

    return new_dec


@doublewrap
def auth(f, permit_type=None):
    '''multiply a function's return value'''
    if permit_type is None:
        permit_type = [AccountType.USER, AccountType.ADMIN]
    elif isinstance(permit_type, list) is False:
        permit_type = [permit_type]

    @wraps(f)
    def wrap(*args, **kwargs):
        request = kwargs.get('request')

        jwt_token_account = None
        if request is not None:
            cookies = request.cookies
            if cookies is not None:
                jwt_token = cookies.get(core.Config.JWT_COOKIE_NAME)
                if jwt_token is not None:
                    try:
                        token = util.decode_access_token(token=jwt_token)
                        jwt_token_account_schema = schema.JwtTokenAccountSchema.parse_obj(token)

                        if AccountType[jwt_token_account_schema.type] in permit_type:
                            jwt_token_account = schema.JwtTokenAccountSchema.parse_obj(token)
                    except:
                        pass

        if jwt_token_account is None:
            raise UnAuthorizedException('인증 실패')
        else:
            request.state.account = jwt_token_account

        return f(*args, **kwargs)
    return wrap
