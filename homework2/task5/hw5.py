"""
Some functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Iterable, Sequence


def custom_range(
    collection: Sequence, lower_bound=None, upper_bound=None, step=1
) -> Iterable:
    """Returns an iterable object constructed in the same way as function range() does.
    Accepts three optional arguments: lower bound, upper bound and element pick interval"""
    # for the case when only first bound specified it must be the upper_bound
    if lower_bound is not None and upper_bound is None:
        upper_bound = lower_bound
        lower_bound = None

    result = []

    should_write = lower_bound is None
    collection_iter = reversed(collection) if step < 0 else iter(collection)

    try:
        counter = 0
        while True:
            elem = next(collection_iter)

            if lower_bound is not None and elem == lower_bound:
                should_write = True

            elif elem == upper_bound:
                raise StopIteration

            if should_write:
                if counter % abs(step) == 0:
                    result.append(elem)
                counter += 1

    except StopIteration:
        pass

    return result
