from homework1.task3.minmax.task03 import find_maximum_and_minimum


def test_max_and_min():
    filename = "testfile.txt"
    max_num, min_num = find_maximum_and_minimum(filename)
    assert max_num == 15
    assert min_num == 2
