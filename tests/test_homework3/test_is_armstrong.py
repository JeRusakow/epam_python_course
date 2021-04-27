from homework3.task04.task04 import is_armstrong


def test_is_armstrong_positive():
    assert is_armstrong(153) is True


def test_is_armstrong_negative():
    assert is_armstrong(10) is False
