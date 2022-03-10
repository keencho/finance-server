from datetime import datetime, timedelta

from jose import jwt

from core.config import Config
from model.account import Account
from schema.account_schema import JwtTokenAccount


def create_access_token(account: Account):
    jwt_token_account = JwtTokenAccount.from_orm(account)
    jwt_token_account.exp = datetime.utcnow() + timedelta(minutes=int(Config.JWT_TOKEN_EXPIRE_MINUTES))

    to_encode = jwt_token_account.dict().copy()
    encoded_jwt = jwt.encode(to_encode, Config.JWT_SECRET_KEY, algorithm=Config.JWT_ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    return jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=Config.JWT_ALGORITHM)