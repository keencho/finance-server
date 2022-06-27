from typing import Optional

from pydantic import BaseModel
from model.account import AccountType


class LoginSchema(BaseModel):
    login_id: str
    password: str


class AccountCreateSchema(BaseModel):
    login_id: str
    password: str
    name: str
    type: AccountType


class JwtTokenAccountSchema(BaseModel):
    id: str
    login_id: str
    name: str
    type: str
    exp: Optional[int]

    class Config:
        orm_mode = True
