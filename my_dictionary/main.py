from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Dict, List
from my_dictionary import controller
from pydantic import BaseModel


app = FastAPI()
# CORSを許可
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)


class Data(BaseModel):
    text: str


@app.get("/")
def hello():
    return {"API": "is running!"}


# @app.get("/analyse")
# def analyse(text: Optional[str]):
#     print(text)
#     return controller.analyse(text=text)

@app.post("/analyse/")
def analyse(data: Data):
    print(data.text)
    return controller.analyse(text=data.text)


@app.get("/read")
def read(text: Optional[str]):
    return controller.read(text=text)
    # TODO: パラグラフ別に分けたい
    # paragraphs = text.split('\n')
    # print(len(paragraphs))
    # return text

@app.get("/translate/{word}")
def translate(word: str):
    return {
        "result": controller.translate(word=word)
    }
