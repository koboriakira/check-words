import nltk
from nltk.corpus import wordnet
from typing import List


def morphy(text: str) -> List[str]:
    tokens = nltk.word_tokenize(text)
    tokens_set = set(tokens)
    rtokens = []
    for token in tokens_set:
        rtokens.append(wordnet.morphy(token))
    return set(rtokens)
