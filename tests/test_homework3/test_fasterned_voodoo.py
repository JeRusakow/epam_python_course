from time import time

from homework3.task02.voodoo_calc import fasterned_voodoo_calc


def test_fasterned_voodoo_execution_time_one_minute():
    start_time = time()
    _ = fasterned_voodoo_calc()
    end_time = time()

    assert end_time - start_time < 60


def test_fasterned_voodoo_correct_result():
    """Tests if fasterned multithreading function returns the same result as single-threaded one."""
    assert fasterned_voodoo_calc() == 1025932
