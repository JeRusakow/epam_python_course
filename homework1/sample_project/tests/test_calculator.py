from calculator.calc import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)


def test_zero_case():
    """Testing that zero is not a power of 2"""
    assert not check_power_of_2(0)


def test_negative_number_case():
    """Testing that a negative number is always not a power of 2"""
    assert not check_power_of_2(-1)
    assert not check_power_of_2(-2)
    assert not check_power_of_2(-7)
    assert not check_power_of_2(-9)
