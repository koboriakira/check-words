from typing import Dict, Any
from my_dictionary.morphy import morphy
from my_dictionary.ngsl import classify_into_ngsl


def analyse(text: str) -> Dict[str, Any]:
    morphied_word_dict: Dict[str, int] = morphy(text=text)
    ngsl_word_list, not_ngsl_word_list = classify_into_ngsl(
        morphied_word_dict.keys())
    return {
        "morphied_word_dict": morphied_word_dict,
        "ngsl_word_list": ngsl_word_list,
        "not_ngsl_word_list": not_ngsl_word_list
    }


print(analyse(text='That is the house that house room.'))
