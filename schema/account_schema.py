from typing import Optional

from pydantic import BaseModel


class LoginSchema(BaseModel):
    login_id: str
    password: str


class AccountCreateBase(BaseModel):
    login_id: str
    password: str
    name: str
    upbit_access_key: Optional[str]
    upbit_private_key: Optional[str]


class JwtTokenAccount(BaseModel):
    id: str
    login_id: str
    name: str
    exp: Optional[int]
    # upbit_access_key: Optional[str]
    # upbit_private_key: Optional[str]

    class Config:
        orm_mode = True
