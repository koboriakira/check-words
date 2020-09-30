import nltk
from nltk.corpus import wordnet
from typing import List, Dict
import re


def morphy(text: str) -> Dict[str, int]:
    tokens = nltk.word_tokenize(text)
    token_counts = _count(tokens=tokens)
    # tokens_set = set(tokens)
    rtokens: Dict[str, int] = {}
    for token in token_counts:
        rtoken = wordnet.morphy(token)
        if rtoken is None:
            continue
        if _is_number(token=str(rtoken)):
            continue
        if rtoken in rtokens:
            rtokens[rtoken] = rtokens[rtoken] + token_counts[token]
        else:
            rtokens[rtoken] = token_counts[token]
    result: Dict[str, int] = {}
    for el in reversed(sorted(rtokens.items(), key=lambda el: el[1])):
        result[el[0]] = el[1]
    return result


# sorted(score.items(), key=lambda x: x[1])


def _count(tokens: List[str]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for token in tokens:
        if token in result:
            result[token] = result[token] + 1
        else:
            result[token] = 1
    return result


def _is_number(token: str) -> bool:
    return re.fullmatch(r'^\d*$', token) is not None
