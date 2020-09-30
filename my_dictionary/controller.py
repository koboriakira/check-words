from typing import List, Dict
from my_dictionary.morphy import morphy
from my_dictionary.ngsl import classify_into_ngsl


def analyse(text: str) -> Dict[str, List[str]]:
    morphied_word_list: List[str] = morphy(text=text)
    ngsl_word_list, not_ngsl_word_list = classify_into_ngsl(morphied_word_list)
    return {
        "morphied_word_list": morphied_word_list,
        "ngsl_word_list": ngsl_word_list,
        "not_ngsl_word_list": not_ngsl_word_list
    }
