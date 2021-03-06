import nltk
from nltk import tokenize
from nltk.corpus import wordnet
from nltk.tree import Tree
from typing import List, Dict, Tuple
import re
from my_dictionary.model.word import Word
from my_dictionary.model.sentence import Sentence
from my_dictionary.model.line import Line
import ngsl


def morphy(text: str) -> Dict[str, int]:
    tokens = nltk.word_tokenize(text)
    token_counts = _count(tokens=tokens)
    rtokens: Dict[str, int] = {}
    for token in token_counts:
        rtoken = wordnet.morphy(token)
        rtoken = ngsl.get_infinitiv(rtoken) if ngsl.include(rtoken) else rtoken
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
                                      str]) -> List[Line]:
    lines: List[str] = _convert_lines(text=text)
    result: List[Line] = []
    for line in lines:
        sentences_token = tokenize.sent_tokenize(line)
        sentences: List[Sentence] = []
        for sentence_tokens in sentences_token:
            sentence: Sentence = _generate_sentence(
                sentence_tokens, proper_nouns)
            sentences.append(sentence)
        line = Line(sentences=sentences)
        result.append(line)
    return result


def _generate_sentence(text: str, proper_nouns: Dict[str, str]) -> Sentence:
    tokens: List[str] = nltk.word_tokenize(text)
    pos: List[Tuple[str, str]] = nltk.pos_tag(tokens)
    words: List[Word] = _convert_words(pos, proper_nouns)
    return Sentence(text=text, words=words)


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


def _convert_lines(text: str) -> List[str]:
    return list(filter(lambda el: el != '', text.split('\n')))


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


def _convert_words(pos: List[Tuple[str, str]],
                   proper_nouns: Dict[str, str]) -> List[Word]:
    result_pos: List[Word] = []
    for pos_el in pos:
        if pos_el[0] in proper_nouns:
            pos_el = (pos_el[0], proper_nouns[pos_el[0]])
        word = Word(value=pos_el[0], pos=pos_el[1])
        result_pos.append(word)
    return result_pos
