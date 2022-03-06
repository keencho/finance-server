import os

from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

UPBIT_ACCESS_KEY = os.environ.get("UPBIT_ACCESS_KEY")
UPBIT_SECRET_KEY = os.environ.get("UPBIT_SECRET_KEY")

app = FastAPI(openapi_url=None)


@app.get("/")
async def root():
    return {
        "UPBIT_ACCESS_KEY": UPBIT_ACCESS_KEY,
        "UPBIT_SECRET_KEY": UPBIT_SECRET_KEY
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
