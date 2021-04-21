from unittest.mock import Mock

from homework2.task4.hw4 import cache


def test_cached_func_returns_the_same_as_original():
    """Checks whether cached function and original one return the same result"""

    def foo(a, b):
        return a + b

    arguments = 10, 5
    cached_foo = cache(foo)

    assert foo(*arguments) == cached_foo(*arguments)


def test_cached_func_called_only_once_on_the_same_data():
    """Tests if the original function is called only once,
    while cached function ma y be called several times with the same args"""
    mock = Mock()
    mock.return_value = 15
    arguments = 10, 5
    cached_mock = cache(mock)
    _ = cached_mock(*arguments)
    _ = cached_mock(*arguments)
    mock.assert_called_once()
