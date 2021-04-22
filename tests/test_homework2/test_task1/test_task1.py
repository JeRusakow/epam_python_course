import os

from pytest import fixture

from homework2.task1.hw1 import *


@fixture()
def get_curr_directory():
    return os.path.dirname(os.path.abspath(__file__))


def test_get_longest_diverse_words_quantity(get_curr_directory):
    """Tests if the function returns exactly 10 words"""
    absolute_filename = os.path.join(get_curr_directory, "longest_words_find_10.txt")

    assert len(get_longest_diverse_words(absolute_filename)) == 10


def test_get_longest_diverse_words_correctness(get_curr_directory):
    """Tests if the function searches for diverse words but not just longest ones"""
    absolute_filename = os.path.join(get_curr_directory, "longest_diverse_words.txt")

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


def test_get_rarest_char(get_curr_directory):
    """Tests if the function really returns the rarest character"""
    absolute_filename = os.path.join(get_curr_directory, "rarest_char_e.txt")

    correct_result = "e"

    assert get_rarest_char(absolute_filename) == correct_result


def test_count_punctuation_chars(get_curr_directory):
    """Tests if the function counts punctuations correctly"""
    absolute_filename = os.path.join(get_curr_directory, "count_punctuation_5.txt")

    assert count_punctuation_chars(absolute_filename) == 5


def test_count_non_ascii(get_curr_directory):
    """Tests if the function counts non-ASCII characters correctly"""
    absolute_filename = os.path.join(get_curr_directory, "count_non_ascii_12.txt")

    assert count_non_ascii_chars(absolute_filename) == 12


def test_get_most_common_non_ascii(get_curr_directory):
    """Tests if the function returns the most common non-ASCII character correctly"""
    absolute_filename = os.path.join(get_curr_directory, "most_common_non_ascii_ą.txt")

    assert get_most_common_non_ascii_char(absolute_filename) == "ą"
