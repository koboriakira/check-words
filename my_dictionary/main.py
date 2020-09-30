from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Dict, List
from my_dictionary import controller


app = FastAPI()
# CORSを許可
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)


@app.get("/")
def hello():
    return {"API": "is running!"}


@app.get("/analyse")
def analyse(text: Optional[str]):
    result: Dict[str, List[str]] = controller.analyse(text=text)
    return result
