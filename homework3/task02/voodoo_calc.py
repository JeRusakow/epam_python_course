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


def fasterned_voodoo_calc(proc_num=50):
    """
    Uses multiprocessing.Pool to speed up voodoo calculations.
    Proc_num sets the number of non-preemptive processes performing the task.
    """
    with mp.Pool(proc_num) as pool:

        return sum(pool.map(slow_calculate, [i for i in range(501)]))
