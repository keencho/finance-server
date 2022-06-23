from typing import Optional

from pydantic import BaseModel


class LoginSchema(BaseModel):
    login_id: str
    password: str


class AccountCreateSchema(BaseModel):
    login_id: str
    password: str
    name: str


class JwtTokenAccountSchema(BaseModel):
    id: str
    login_id: str
    name: str
    exp: Optional[int]

    class Config:
        orm_mode = True
