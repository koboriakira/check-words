from typing import Dict, Any, List
from googletrans import Translator
import ngsl
from ngsl import Result
from my_dictionary.morphy import morphy, pos, proper_noun
from my_dictionary.model.line import Line
from my_dictionary import api

translator = Translator()
ENDPOINT_SIMPLE_WORD_LIST = 'https://simple-word-list-bre4azfwrq-an.a.run.app/'


def analyse(text: str) -> Dict[str, Any]:
    morphied_word_dict: Dict[str, int] = morphy(text=text)
    words: List[str] = morphied_word_dict.keys()
    result: Result = ngsl.classify(words=words, include_supplemental=True)
    proper_nouns: Dict[str, str] = proper_noun(text=text)
    lines: List[Line] = pos(
        text=text, proper_nouns=proper_nouns)
    return {
        "lines": lines,
        "morphied_word_dict": morphied_word_dict,
        "ngsl_word_list": result.ngsl_words,
        "not_ngsl_word_list": result.not_ngsl_words,
        "proper_nouns": proper_nouns,
    }


def add_word_list(
        url: str,
        ngsl_words: List[str],
        not_ngsl_words: List[str]) -> None:
    try:
        res = api.post(
            url=f'{ENDPOINT_SIMPLE_WORD_LIST}words/sites/check',
            data={
                "url": url})
        if res['checked']:
            return
        res = api.post(
            url=f'{ENDPOINT_SIMPLE_WORD_LIST}words/ngsl/add',
            data={
                "words": ngsl_words})
        if not res['success']:
            return
        res = api.post(
            url=f'{ENDPOINT_SIMPLE_WORD_LIST}words/notngsl/add',
            data={
                "words": not_ngsl_words})
        if not res['success']:
            return
        res = api.post(
            url=f'{ENDPOINT_SIMPLE_WORD_LIST}words/sites/add',
            data={
                "url": url})
    except Exception as e:
        print(e)


def translate(word: str) -> str:
    """
    Google Translate APIを呼び出す
    """
    try:
        return translator.translate(word, dest="ja").text
    except Exception:
        return 'can\'t translate'
