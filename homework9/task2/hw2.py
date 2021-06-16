"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager
from typing import Type


class ExceptionSuppressor:
    """
    A context manager to suppress an exact type of exceptions.

    Args:
         exception_type: an exception type to suppress

    Returns:
        None
    """

    def __init__(self, *exception_type: Type[BaseException]):
        self.exception_type = exception_type

    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exception_type:
            return True
        raise


@contextmanager
def suppress_exception(*exception_type: Type[BaseException]) -> None:
    """
    Exception suppressing context manager.

    Args:
        exception_type: A type of exception to be suppressed

    Returns:
        None
    """
    try:
        yield None
    except exception_type:
        pass
    except Exception:
        raise
