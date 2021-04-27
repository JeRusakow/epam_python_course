from homework2.task3.hw3 import combinations


def test_combinations_result_quantity():
    result = combinations([1, 2], [3, 4])
    assert len(result) == 4


def test_combinations_result_from_lists_2and2():
    test_combinations = [[1, 3], [1, 4], [2, 3], [2, 4]]
    result = combinations([1, 2], [3, 4])
    assert all(combination in result for combination in test_combinations)


def test_combinations_result_from_lists_1and2and1():
    test_combinations = [[1, 3, 5], [1, 4, 5]]
    result = combinations([1], [3, 4], [5])
    assert all(combination in result for combination in test_combinations)
