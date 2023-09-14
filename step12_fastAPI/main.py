# FastAPI도 다운로드 한다.
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World"

@app.get("/json")
def getJson():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# 해당 위치 에서 터미널로 실행
# uvicorn main:app --reload










