from minmax.task03 import find_maximum_and_minimum


def test_max_and_min():
    filename = "testfile.txt"
    max, min = find_maximum_and_minimum(filename)
    assert max == 15
    assert min == 2
