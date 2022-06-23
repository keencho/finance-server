from datetime import datetime, timedelta

from jose import jwt

import core
import schema
from core.config import Config
from model.account import Account


def create_access_token(account: Account):
    jwt_token_account = schema.JwtTokenAccountSchema.from_orm(account)
    jwt_token_account.exp = datetime.utcnow() + timedelta(minutes=int(core.Config.JWT_TOKEN_EXPIRE_MINUTES))

    to_encode = jwt_token_account.dict().copy()
    encoded_jwt = jwt.encode(to_encode, Config.JWT_SECRET_KEY, algorithm=core.Config.JWT_ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    return jwt.decode(token, core.Config.JWT_SECRET_KEY, algorithms=core.Config.JWT_ALGORITHM)