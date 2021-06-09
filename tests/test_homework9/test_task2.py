import pytest

from homework9.task2.hw2 import ExceptionSuppressor, suppress_exception


# ExceptionSuppressor class testing
def test_exception_suppressor_suppresses_exceptions():
    with ExceptionSuppressor(TypeError):
        raise TypeError


def test_exception_suppressor_suppresses_several_exceptions():
    with ExceptionSuppressor(TypeError, ValueError, AttributeError):
        raise AttributeError


def test_exception_suppressor_passes_allowed_exceptions():
    with pytest.raises(ValueError):  # noqa: PT012 PT011
        with ExceptionSuppressor(TypeError):
            raise ValueError


# suppress_exception generator testing
def test_suppress_exception_suppresses_exceptions():
    with suppress_exception(TypeError):
        raise TypeError


def test_suppress_exception_suppresses_several_exceptions():
    with suppress_exception(TypeError, ValueError, AttributeError):
        raise ValueError


def test_suppress_exception_passes_allowed_exceptions():
    with pytest.raises(ValueError):  # noqa: PT012 PT011
        with suppress_exception(TypeError):
            raise ValueError
