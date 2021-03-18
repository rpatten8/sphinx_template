"""
functions.py
======================================
Contains all functions used by module.
"""


def adder(word, num):
    """Combines a word with a number into one string.

    :param word: Word to to be prefixed
    :type word: str

    :param num: Number to be suffixed
    :type num: int

    :raises AssertionError: If word not of type str

    :warning: Does not check if num of type int

    :return: Combined sentence
    :rtype: str
    """
    if not isinstance(word, str):
        raise AssertionError('Word not of type str!')
    result = f"{word} {str(num)}"
    return result