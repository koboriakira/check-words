from typing import Dict, Any, List, Tuple
from my_dictionary.morphy import morphy, pos, proper_noun
from my_dictionary.ngsl import classify_into_ngsl
from googletrans import Translator

translator = Translator()


def analyse(text: str) -> Dict[str, Any]:
    morphied_word_dict: Dict[str, int] = morphy(text=text)
    ngsl_word_list, not_ngsl_word_list = classify_into_ngsl(
        morphied_word_dict.keys())
    pos_text: List[List[Tuple[str, str]]] = pos(text=text)
    proper_nouns: Dict[str, str] = proper_noun(text=text)
    return {
        "pos_text": pos_text,
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
