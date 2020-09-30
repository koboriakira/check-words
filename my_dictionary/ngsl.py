from ngsl import ngsl
from typing import List, Tuple


def classify_into_ngsl(word_list: List[str]) -> Tuple[List[str], List[str]]:
    """
    NGSLに含まれている単語とそうでない単語に分けます
    """
    ngsl_word_list, not_ngsl_word_list = [], []
    for word in word_list:
        if ngsl.include(word):
            ngsl_word_list.append(word)
        else:
            not_ngsl_word_list.append(word)
    return sorted(ngsl_word_list), sorted(not_ngsl_word_list)
