from pydantic import BaseModel


class MarketCreateBase(BaseModel):
    code: str
    korean_name: str
    english_name: str
