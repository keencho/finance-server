from pydantic import BaseModel


class TickerBase(BaseModel):
    code: str
    korean_name: str
    english_name: str

