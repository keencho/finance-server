from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import Config

engine = create_engine(
    url=f'postgresql+psycopg2://{Config.DB_USER_NAME}:{Config.DB_USER_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_SCHEMA}',
    echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()