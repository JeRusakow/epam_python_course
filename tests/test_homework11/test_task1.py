import pytest

from homework11.hw1 import SimplifiedEnum

test_keys = ["MOSCOW", "KYIV", "WARSZAWA"]


class CityEnum(metaclass=SimplifiedEnum):
    __keys = tuple(test_keys)


def test_enum():
    assert CityEnum.WARSZAWA == "WARSZAWA"


def test_len():
    assert len(CityEnum) == 3


def test_contains():
    assert test_keys[1] in CityEnum


def test_iter():
    assert list(iter(CityEnum)) == ["MOSCOW", "KYIV", "WARSZAWA"]


def test_keys_not_identified():
    with pytest.raises(AttributeError, match="'__keys' attribute must be stated"):

        class KeylessEnum(metaclass=SimplifiedEnum):
            pass


def test_wrong_identifier():
    with pytest.raises(AttributeError, match="Enum item '012' cannot be an identifier"):

        class WrongEnum(metaclass=SimplifiedEnum):
            __keys = ("012",)


def test_keyword_identifier():
    with pytest.raises(
        AttributeError, match="Enum item 'class' cannot be an identifier"
    ):

        class WrongEnum(metaclass=SimplifiedEnum):
            __keys = ("class",)
