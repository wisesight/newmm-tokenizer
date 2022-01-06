import re
from typing import List, Optional

from .trie import Trie
from .newmm import segment

DEFAULT_WORD_TOKENIZE_ENGINE = "newmm"

def word_tokenize(
    text: str,
    custom_dict: Optional[Trie] = None,
    engine: str = DEFAULT_WORD_TOKENIZE_ENGINE,
    keep_whitespace: bool = True,
) -> List[str]:

    if not text or not isinstance(text, str):
        return []

    segments = []
    if custom_dict:
        segments = segment(text, custom_dict)
    else:
        segments = segment(text)

    if not keep_whitespace:
        segments = [token.strip(" ") for token in segments if token.strip(" ")]

    return segments
