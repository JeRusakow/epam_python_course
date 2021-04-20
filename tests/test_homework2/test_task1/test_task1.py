import os

from homework2.task1.hw1 import *


def test_get_longest_diverse_words_quantity():
    """Tests if the function returns exactly 10 words"""
    current_directory = os.path.dirname(os.path.abspath(__file__))
    absolute_filename = os.path.join(current_directory, "longest_words_find_10.txt")

    assert len(get_longest_diverse_words(absolute_filename)) == 10


def test_get_longest_diverse_words_correctness():
    """Tests if the function searches for diverse words but not just longest ones"""
    current_directory = os.path.dirname(os.path.abspath(__file__))
    absolute_filename = os.path.join(current_directory, "longest_diverse_words.txt")

    correct_result = [
        "abcdefghijk",
        "abcdefghij",
        "abcdefghi",
        "abcdefgh",
        "abcdefg",
        "abcdef",
        "acbde",
        "abcd",
        "abc",
        "ab",
    ]

    result = get_longest_diverse_words(absolute_filename)

    print(result)

    assert result == correct_result


def test_get_rarest_char():
    """Tests if the function really returns the rarest character"""
    current_directory = os.path.dirname(os.path.abspath(__file__))
    absolute_filename = os.path.join(current_directory, "rarest_char_e.txt")

    correct_result = "e"

    assert get_rarest_char(absolute_filename) == correct_result


def test_count_punctuation_chars():
    """Tests if the function counts punctuations correctly"""
    current_directory = os.path.dirname(os.path.abspath(__file__))
    absolute_filename = os.path.join(current_directory, "count_punctuation_5.txt")

    assert count_punctuation_chars(absolute_filename) == 5


def test_count_non_ascii():
    """Tests if the function counts non-ASCII characters correctly"""
    current_directory = os.path.dirname(os.path.abspath(__file__))
    absolute_filename = os.path.join(current_directory, "count_non_ascii_12.txt")

    assert count_non_ascii_chars(absolute_filename) == 12


def test_get_most_common_non_ascii():
    """Tests if the function returns the most common non-ASCII character correctly"""
    current_directory = os.path.dirname(os.path.abspath(__file__))
    absolute_filename = os.path.join(current_directory, "most_common_non_ascii_ą.txt")

    assert get_most_common_non_ascii_char(absolute_filename) == "ą"
