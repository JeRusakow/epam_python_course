import os

from homework1.task3.minmax.task03 import find_maximum_and_minimum


def test_max_and_min():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    absolute_filename = os.path.join(current_directory, "testfile.txt")

    max_num, min_num = find_maximum_and_minimum(absolute_filename)
    assert max_num == 15
    assert min_num == 2
