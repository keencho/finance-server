from pydantic import BaseModel


class TickerCreateBase(BaseModel):
    code: str
    korean_name: str
    english_name: str
