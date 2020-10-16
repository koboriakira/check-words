import ngsl
from ngsl import Result
from typing import List, Tuple


def classify_into_ngsl(word_list: List[str]) -> Tuple[List[str], List[str]]:
    """
    NGSLに含まれている単語とそうでない単語に分けます
    """
    result: Result = ngsl.classify(words=word_list, include_supplemental=True)
    return result.ngsl_word_list, result.not_ngsl_word_list
