import string

from homework2.task5.hw5 import custom_range


def test_custom_range_with_raw_data():
    assert custom_range(string.ascii_lowercase) == [
        char for char in string.ascii_lowercase
    ]


def test_custom_range_with_upper_bound_only():
    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


def test_custom_range_with_both_bounds():
    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_custom_range_with_both_bounds_and_positive_step():
    assert custom_range(string.ascii_lowercase, "g", "p", 2) == [
        "g",
        "i",
        "k",
        "m",
        "o",
    ]


def test_custom_range_with_both_bounds_and_negative_step():
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
