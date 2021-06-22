"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""
from keyword import iskeyword


class SimplifiedEnum(type):
    """
    A metaclass to create Enums in a simpler way.
    To use its benefits derived class should have tuple '__keys' class attribute
    """

    def __new__(cls, name, bases, dct):
        if f"_{name}__keys" not in dct:
            raise AttributeError("'__keys' attribute must be stated")

        for item in dct[f"_{name}__keys"]:
            if not item.isidentifier() or iskeyword(item):
                raise AttributeError(f"Enum item '{item}' cannot be an identifier")
            dct[item] = item

        cls_instance = super().__new__(cls, name, bases, dct)
        cls_instance._keys = dct[f"_{name}__keys"]
        return cls_instance

    def __len__(cls):
        return len(cls._keys)

    def __contains__(cls, item):
        return item in cls._keys

    def __iter__(cls):
        return iter(cls._keys)
