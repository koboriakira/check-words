from dataclasses import dataclass
from my_dictionary.model.sentence import Sentence
from typing import List


@dataclass
class Line:
    sentences: List[Sentence]
