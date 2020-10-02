import nltk
from nltk import tokenize
from nltk.corpus import wordnet
from nltk.tree import Tree
from typing import List, Dict, Tuple
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


def pos(text: str, proper_nouns: Dict[str,
                                      str]) -> List[List[Tuple[str, str]]]:
    sentence_tokens = tokenize.sent_tokenize(text)
    result: List[List[Tuple[str, str]]] = []
    for sentence in sentence_tokens:
        tokens: List[str] = nltk.word_tokenize(sentence)
        pos: List[Tuple[str, str]] = nltk.pos_tag(tokens)
        pos = _convert_proper_nouns(pos, proper_nouns)
        result.append(pos)
    return result


def proper_noun(text: str) -> Dict[str, str]:
    tokens = nltk.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(pos)

    result: Dict[str, str] = {}
    for entity in entities:
        # 固有名詞はTree型が格納されている
        if not isinstance(entity, Tree):
            continue
        label = entity.label()
        word = entity[0][0]
        result[word] = label
    return result


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


def _convert_proper_nouns(
        pos: List[Tuple[str, str]], proper_nouns: Dict[str, str]) -> List[Tuple[str, str]]:
    result_pos: List[Tuple[str, str]] = []
    for pos_el in pos:
        if pos_el[0] in proper_nouns:
            pos_el = (pos_el[0], proper_nouns[pos_el[0]])
        result_pos.append(pos_el)
    return result_pos
