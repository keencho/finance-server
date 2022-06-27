from functools import wraps

from starlette.requests import Request

import core
import schema
import util
from core.exception import UnAuthorizedException
from core.request_middleware import get_request_state
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
        request_state = get_request_state()
        jwt_token_account = None

        if request_state is not None:
            temp_jwt_token_account = request_state['account']

            if temp_jwt_token_account is not None:
                if AccountType[temp_jwt_token_account.type] in permit_type:
                    jwt_token_account = temp_jwt_token_account

        if jwt_token_account is None:
            raise UnAuthorizedException('인증 실패')

        return f(*args, **kwargs)
    return wrap
