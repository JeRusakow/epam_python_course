def check_power_of_2(a: int) -> bool:
    """Checks if the number is a power of 2"""
    if a < 1:
        return False
    return not (bool(a & (a - 1)))
