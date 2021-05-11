from unittest import mock

from pytest import fixture

from homework5.task2.save_original_info import info_transfer


@fixture
def test_function():
    """This is a test function"""
    return test_function


def test_decorator_copies_the_docstring_from_stated(test_function):
    @info_transfer(func_from=test_function)
    def copied_func():
        """To be redefined"""
        return None

    assert copied_func.__doc__ == test_function.__doc__


def test_decorator_copies_the_name_from_stated(test_function):
    @info_transfer(func_from=test_function)
    def copied_func():
        """To be redefined"""
        return None

    assert copied_func.__name__ == test_function.__name__


def test_decorator_copies_the_original_function_from_stated(test_function):
    @info_transfer(func_from=test_function)
    def copied_func():
        """To be redefined"""
        return None

    assert copied_func.__original_func is test_function
