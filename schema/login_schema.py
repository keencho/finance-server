from pydantic import BaseModel


class LoginSchema(BaseModel):
    login_id: str
    password: str
