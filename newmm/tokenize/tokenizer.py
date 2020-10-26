import re
from typing import List

from .trie import Trie
from .newmm import segment

DEFAULT_WORD_TOKENIZE_ENGINE = "newmm"

def word_tokenize(
    text: str,
    custom_dict: Trie = None,
    engine: str = DEFAULT_WORD_TOKENIZE_ENGINE,
    keep_whitespace: bool = True,
) -> List[str]:

    if not text or not isinstance(text, str):
        return []

    segments = []
    segments = segment(text, custom_dict)

    if not keep_whitespace:
        segments = [token.strip(" ") for token in segments if token.strip(" ")]

    return segments
