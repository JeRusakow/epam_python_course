from pathlib import Path

import pytest

from homework9.task1.hw1 import merge_sorted_files


@pytest.fixture(scope="session")
def test_file_dir(tmpdir_factory):
    return Path("tests/test_data/hw_9/task1")


def test_merge_files(test_file_dir):
    file_1 = test_file_dir / "file1.txt"
    file_2 = test_file_dir / "file2.txt"
    file_3 = test_file_dir / "file3.txt"

    expected_res = list(range(1, 10))
    res = list(merge_sorted_files([file_1, file_2, file_3]))
    assert res == expected_res
