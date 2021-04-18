from fibonacci.task02 import check_fibonacci


def test_complete_sequence():
    """Tests if true sequence starting from [0, 1, 1, ... ] passes the check"""
    test_data = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert check_fibonacci(test_data)


def test_sequence_fragment():
    """Tests if true sequence not starting from [0, 1, 1, ... ] also passes the check"""
    test_data = [5, 8, 13, 21, 34, 55, 89]
    assert check_fibonacci(test_data)


def test_wrong_sequence():
    """Tests if a wrong sequence does not pass the test"""
    test_data = [1, 1, 5, 8, 6, 3]
    assert not check_fibonacci(test_data)


def test_rightful_sequence_with_wrong_beginning():
    """Tests if a sequence built with correct rules but with wrong initial values fails the check"""
    test_data = [5, 6, 11, 17, 28, 45, 73]
    assert not check_fibonacci(test_data)


def test_reversed_fibonacci_sequence():
    """Tests if a reversed descending sequence fails the tests"""
    test_data = [89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0]
    assert not check_fibonacci(test_data)
