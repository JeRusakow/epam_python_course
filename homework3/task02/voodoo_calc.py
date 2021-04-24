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


def fasterned_voodoo_calc():
    """Uses multiprocessing to speed up voodoo calculations"""
    shared_value = mp.Value("i", 0)

    def worker(shared_val, call_arg):
        """A worker for computing slow_calculate with a specific parameter.
        Uses shared value to store result"""
        res = slow_calculate(call_arg)

        with shared_val.get_lock():
            shared_val.value += res

    processes = [
        mp.Process(target=worker, args=(shared_value, val)) for val in range(501)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    return shared_value.value
