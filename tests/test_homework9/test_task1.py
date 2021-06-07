import pytest

from homework9.task1.hw1 import merge_sorted_files


@pytest.fixture(scope="session")
def temp_files(tmpdir_factory):
    directory = tmpdir_factory.mktemp("tmp_dir")
    file_1 = directory.join("file1.txt")
    file_2 = directory.join("file2.txt")
    file_3 = directory.join("file3.txt")

    with open(file_1, "w") as f:
        f.write("1\n4\n9")
    with open(file_2, "w") as f:
        f.write("2\n5")
    with open(file_3, "w") as f:
        f.write("3\n6\n7\n8")

    return [file_1, file_2, file_3]


def test_merge_files(temp_files):
    expected_res = list(range(1, 10))
    res = list(merge_sorted_files(temp_files))
    assert res == expected_res
