import os
import urllib.parse

from dotenv import load_dotenv

load_dotenv()


class Config:
    UPBIT_ACCESS_KEY = os.environ.get('UPBIT_ACCESS_KEY')
    UPBIT_SECRET_KEY = os.environ.get('UPBIT_SECRET_KEY')

    DB_USER_NAME = os.environ.get('DB_USER_NAME')
    DB_USER_PASSWORD = os.environ.get('DB_USER_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_SCHEMA = os.environ.get('DB_SCHEMA')
    DB_FULL_URL = f'postgresql+psycopg2://{DB_USER_NAME}:{DB_USER_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SCHEMA}'

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')
    JWT_TOKEN_EXPIRE_MINUTES = os.environ.get('JWT_TOKEN_EXPIRE_MINUTES')
    JWT_COOKIE_NAME = os.environ.get('JWT_COOKIE_NAME')

    SUPER_ADMIN_ID = os.environ.get('SUPER_ADMIN_ID')
    SUPER_ADMIN_PW = os.environ.get('SUPER_ADMIN_PW')
    SUPER_ADMIN_NAME = os.environ.get('SUPER_ADMIN_NAME')
