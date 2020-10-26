import os
from typing import Union

_CORPUS_DIRNAME = "corpus"
_CORPUS_PATH = os.path.join('', _CORPUS_DIRNAME)

def corpus_path() -> str:
    """
    Get path where corpus files are kept locally.
    """
    # return _CORPUS_PATH
    return 'newmm_tokenizer'

def get_corpus(filename: str, as_is: bool = False) -> Union[frozenset, list]:
    """
    Read corpus data from file and return a frozenset or a list.
    Each line in the file will be a member of the set or the list.
    By default, a frozenset will be return, with whitespaces stripped, and
    empty values and duplicates removed.
    If as_is is True, a list will be return, with no modifications
    in member values and their orders.
    (Please see the filename from
    `this file
    <https://github.com/PyThaiNLP/pythainlp-corpus/blob/master/db.json>`_
    :param str filename: filename of the corpus to be read
    :return: :class:`frozenset` or :class:`list` consists of lines in the file
    :rtype: :class:`frozenset` or :class:`list`
    :Example:
    ::
        from pythainlp.corpus import get_corpus
        get_corpus('negations_th.txt')
        # output:
        # frozenset({'แต่', 'ไม่'})
        get_corpus('ttc_freq.txt')
        # output:
        # frozenset({'โดยนัยนี้\\t1',
        #    'ตัวบท\\t10',
        #    'หยิบยื่น\\t3',
        #     ...})
    """
    path = os.path.join(corpus_path(), filename)
    lines = []
    with open(path, "r", encoding="utf-8-sig") as fh:
        lines = fh.read().splitlines()

    if as_is:
        return lines

    lines = [line.strip() for line in lines]
    return frozenset(filter(None, lines))