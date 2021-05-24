from homework7.task2.hw2 import backspace_compare


def test_simple_case():
    str_a = "ab#c"
    str_b = "ad#c"
    assert backspace_compare(str_a, str_b)


def test_backspace_on_empty_line():
    str_a = "####vv"
    str_b = "#vv"
    assert backspace_compare(str_a, str_b)


def test_unequal_strings():
    str_a = "abcd"
    str_b = "aaaa"
    assert not backspace_compare(str_a, str_b)
