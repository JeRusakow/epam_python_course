from homework1.task4.sum_of_four.task04 import check_sum_of_four


def test_sum_of_four():
    data_a = [2, 5, 13]
    data_b = [13, 5, 2]
    data_c = [2, 13, 5]
    data_d = [-6, -15, -39]

    assert check_sum_of_four(data_a, data_b, data_c, data_d) == 3
