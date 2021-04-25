from collections import defaultdict
from typing import Callable


def dec_cached(times=1) -> Callable:
    """
    Caches a function using dictionary. Each function call result is cached for 'times' further calls.
    After 'times' count expires, original function is called once more and result is saved again for 'times' calls
    """

    def wrapper(func_orig: Callable):
        """
        Stores original function output and storing countdown value in a dictionary.
        """
        result_dict = {}

        def cached_func(*args):
            # if function with args was not called previously, call the function
            if args not in result_dict.keys():
                result_dict[args] = [func_orig(*args), times]
            # if storing countdown has expired, call te function again
            if result_dict[args][1] == 0:
                result_dict[args] = [func_orig(*args), times]

            result_dict[args][1] -= 1
            return result_dict[args][0]

        return cached_func

    return wrapper
