import hashlib
import multiprocessing as mp
import random
import struct
import time


# Slow calculating function
# Experimentally is found out that computing sum of slow_calculation for each number from 0 to 500
# takes approx. 1020 sec and result is 1025932
def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fasterned_voodoo_calc(subroutine_arg_size=10) -> int:
    """
    Uses multiprocessing.Process to spawn processes each assigned a chunk of general argument array
    """

    def worker(shared_value: mp.Value, *args) -> None:
        for arg in args:
            res = slow_calculate(arg)

            with shared_value.get_lock():
                shared_value.value += res

    shared_var = mp.Value("i", 0)

    arg_list = [i for i in range(501)]
    arg_sublists = [
        arg_list[i : i + subroutine_arg_size]
        for i in range(0, len(arg_list), subroutine_arg_size)
    ]

    processes = [
        mp.Process(target=worker, args=(shared_var, *arg_sublist))
        for arg_sublist in arg_sublists
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    return shared_var.value
