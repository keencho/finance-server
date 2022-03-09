from datetime import datetime, timedelta

from jose import jwt

from core.config import Config


class JwtService:
    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=int(Config.JWT_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, Config.JWT_SECRET_KEY, algorithm=Config.JWT_ALGORITHM)
        return encoded_jwt

    def decode(self, token: str):
        return jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=Config.JWT_ALGORITHM)