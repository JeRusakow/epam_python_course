from typing import Callable


def dec_cached(times=1) -> Callable:
    def wrapper(func_orig: Callable):
        result_dict = {}

        def cached_func(*args):
            if args not in result_dict.keys() or result_dict[args][1] == 0:
                result_dict[args] = [func_orig(*args), times]

            result_dict[args][1] -= 1
            return result_dict[args][0]

        return cached_func

    return wrapper
