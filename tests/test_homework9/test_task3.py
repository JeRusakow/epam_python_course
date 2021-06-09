import random
from pathlib import Path

import pytest

from homework9.task3.hw3 import universal_file_counter


@pytest.fixture(scope="session")
def test_dir_path():
    return Path("tests/test_data/hw_9/task3")


def test_dir_does_not_exist(test_dir_path):
    random_dir_name = "".join((chr(random.randint(97, 120)) for _ in range(10)))
    path = test_dir_path / random_dir_name
    with pytest.raises(FileNotFoundError, match=f"Path '{path}' does not exists"):
        universal_file_counter(path, "ext")


def test_empty_directory(test_dir_path):
    path = test_dir_path / "empty_dir"
    assert universal_file_counter(path, "ext") == 0


def test_single_file_no_tokenizer(test_dir_path):
    path = test_dir_path / "subdir" / "subsubdir"
    assert universal_file_counter(path, "txt") == 3


def test_single_file_with_tokenizer(test_dir_path):
    path = test_dir_path / "subdir" / "subsubdir"
    assert universal_file_counter(path, "txt", str.split) == 5


def test_no_satisfying_files(test_dir_path):
    assert universal_file_counter(test_dir_path, "none") == 0


def test_several_txt_files_no_tokenizer(test_dir_path):
    assert universal_file_counter(test_dir_path, "txt") == 6


def test_several_txt_files_with_tokenizer(test_dir_path):
    assert universal_file_counter(test_dir_path, "txt", str.split) == 10


def test_recursive_search(test_dir_path):
    assert universal_file_counter(test_dir_path, "txt", str.split, recursive=True) == 18
