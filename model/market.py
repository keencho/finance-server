from sqlalchemy import Column, String

from core.database import Base


class Market(Base):
    __tablename__ = 'market'

    code = Column(String, primary_key=True, index=True)
    korean_name = Column(String)
    english_name = Column(String)
