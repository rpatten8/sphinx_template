"""
app.py
==============================
Handles all app related stuff
"""


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """A simple function that prints to webpage"""
    result = adder('Hello World!', 100)
    return result

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


if __name__ == '__main__':
    app.run()
