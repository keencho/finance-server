from typing import Optional

from pydantic import BaseModel


class AccountCreateBase(BaseModel):
    login_id: str
    password: str
    upbit_access_key: Optional[str]
    upbit_private_key: Optional[str]


class Account(BaseModel):
    id: str
    login_id: str
    upbit_access_key: Optional[str]
    upbit_private_key: Optional[str]

    class Config:
        orm_mode = True