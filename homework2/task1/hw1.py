"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from the largest amount of unique symbols
    2) Find the rarest symbol for a document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Returns a list of 10 longest words consisting of the most various letters"""
    word_unique_letters_dict = {}

    with open(file_path, "r", encoding="unicode-escape") as datafile:
        for line in datafile.readlines():
            words = line.translate(str.maketrans("", "", string.punctuation)).split()

            for word in words:
                if word not in word_unique_letters_dict.keys():
                    word_unique_letters_dict[word] = len(set(word))

    sorted_dictionary = sorted(word_unique_letters_dict.items(), key=lambda x: -x[1])

    return [word for word, _ in sorted_dictionary[:10]]


def get_rarest_char(file_path: str) -> str:
    """Returns the rarest symbol for a file. If there are several equally rare symbols, returns one of them"""
    chars_dict = {}

    with open(file_path, "r", encoding="unicode-escape") as datafile:
        for symbol in datafile.read():
            if symbol not in chars_dict.keys():
                chars_dict[symbol] = 1
            else:
                chars_dict[symbol] += 1

    chars_dict = sorted(chars_dict.items(), key=lambda x: x[1])

    return chars_dict[0][0]


def count_punctuation_chars(file_path: str) -> int:
    """Returns the amount of punctuations symbols from across the file"""
    punctuation_counter = 0

    with open(file_path, "r", encoding="unicode-escape") as datafile:
        for symbol in datafile.read():
            if symbol in string.punctuation:
                punctuation_counter += 1

    return punctuation_counter


def count_non_ascii_chars(file_path: str) -> int:
    """Returns the amount of non-ascii characters from across the file"""
    non_ascii_counter = 0

    with open(file_path, "r", encoding="unicode-escape") as datafile:
        for symbol in datafile.read():
            if not symbol.isascii():
                non_ascii_counter += 1

    return non_ascii_counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Shuffles through the file and returns the most common non-ascii character"""
    non_ascii_char_dict = {}

    with open(file_path, "r", encoding="unicode-escape") as datafile:
        for symbol in datafile.read():
            if not symbol.isascii():
                if symbol not in non_ascii_char_dict.keys():
                    non_ascii_char_dict[symbol] = 1
                else:
                    non_ascii_char_dict[symbol] += 1

    non_ascii_char_dict = sorted(non_ascii_char_dict.items(), key=lambda x: x[1])

    return non_ascii_char_dict[-1][0]
