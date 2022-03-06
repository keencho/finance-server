import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    UPBIT_ACCESS_KEY = os.environ.get("UPBIT_ACCESS_KEY")
    UPBIT_SECRET_KEY = os.environ.get("UPBIT_SECRET_KEY")