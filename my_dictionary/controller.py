from typing import Dict, Any, List
from googletrans import Translator
from my_dictionary.morphy import morphy, pos, proper_noun
from my_dictionary.ngsl import classify_into_ngsl
from my_dictionary.model.line import Line

translator = Translator()


def analyse(text: str) -> Dict[str, Any]:
    morphied_word_dict: Dict[str, int] = morphy(text=text)
    ngsl_word_list, not_ngsl_word_list = classify_into_ngsl(
        morphied_word_dict.keys())
    proper_nouns: Dict[str, str] = proper_noun(text=text)
    lines: List[Line] = pos(
        text=text, proper_nouns=proper_nouns)
    return {
        "lines": lines,
        "morphied_word_dict": morphied_word_dict,
        "ngsl_word_list": ngsl_word_list,
        "not_ngsl_word_list": not_ngsl_word_list,
        "proper_nouns": proper_nouns,
    }


def translate(word: str) -> str:
    """
    Google Translate APIを呼び出す
    """
    try:
        return translator.translate(word, dest="ja").text
    except Exception:
        return 'can\'t translate'
