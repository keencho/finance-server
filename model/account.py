import uuid

from sqlalchemy import Column, String, Integer

from core.database import Base


class Account(Base):
    __tablename__ = 'account'

    id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()))
    login_id = Column(String, unique=True, nullable=False)
    name = Column(String, unique=False, nullable=False)
    password = Column(String, nullable=False)
    upbit_access_key = Column(String, nullable=True)
    upbit_private_key = Column(String, nullable=True)
    telegram_token = Column(String, nullable=True)
    telegram_chat_id = Column(Integer, nullable=True)

