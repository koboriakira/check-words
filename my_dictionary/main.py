from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from my_dictionary import controller
from pydantic import BaseModel
from translate_bookmark.translate_bookmark import get_text


app = FastAPI()
# CORSを許可
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Data(BaseModel):
    text: str


class Url(BaseModel):
    url: str


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
    try:
        return controller.analyse(text=data.text)
    except LookupError as e:
        print(e)
        print(e.args)
        return {"error": "LookupError"}


@app.post("/analyse-site/")
def analyse_site(data: Url):
    print(data.url)
    text = get_text(url=data.url)
    result = controller.analyse(text=text)
    controller.add_word_list(
        url=data.url,
        ngsl_words=result['ngsl_word_list'],
        not_ngsl_words=result['not_ngsl_word_list'])
    result['text'] = text
    return result


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
