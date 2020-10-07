from dataclasses import dataclass
from my_dictionary.model.word import Word
from typing import List


@dataclass
class Sentence:
    words: List[Word]
    text: str
