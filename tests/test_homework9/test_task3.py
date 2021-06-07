import random

import pytest

from homework9.task3.hw3 import universal_file_counter


@pytest.fixture(scope="session")
def single_txt_file_directory(tmpdir_factory):
    directory = tmpdir_factory.mktemp("single_file_dir")
    filepath = directory.join("file.txt")
    with open(filepath, "w") as file:
        file.write("one\ntwo three\nfour")

    return directory


@pytest.fixture(scope="session")
def several_txt_files_directory(tmpdir_factory):
    directory = tmpdir_factory.mktemp("several_files_dir")
    filenames = ["first.txt", "second.htm", "third.txt"]
    file_content = [
        "jeden\ndwa trzy cztere\npięńć sześć",
        "<html>\n<title>\nNone\n</title>\n</html>",
        "siedem\nosiem dziewieć\ndziesiąc",
    ]
    for filename, content in zip(filenames, file_content):
        filepath = directory.join(filename)
        with open(filepath, "w") as file:
            file.write(content)

    return directory


@pytest.fixture(scope="session")
def empty_directory(tmpdir_factory):
    return tmpdir_factory.mktemp("empty_dir")


def test_dir_does_not_exist():
    random_dir_name = "".join((chr(random.randint(97, 120)) for _ in range(10)))
    with pytest.raises(
        FileNotFoundError, match=f"Path '{random_dir_name}' does not exists"
    ):
        universal_file_counter(random_dir_name, "ext")


def test_empty_directory(empty_directory):
    assert universal_file_counter(empty_directory, "ext") == 0


def test_single_file_no_tokenizer(single_txt_file_directory):
    assert universal_file_counter(single_txt_file_directory, "txt") == 3


def test_single_file_with_tokenizer(single_txt_file_directory):
    assert universal_file_counter(single_txt_file_directory, "txt", str.split) == 4


def test_no_satisfying_files(single_txt_file_directory):
    assert universal_file_counter(single_txt_file_directory, "none") == 0


def test_several_txt_files_no_tokenizer(several_txt_files_directory):
    assert universal_file_counter(several_txt_files_directory, "txt") == 6


def test_several_txt_files_with_tokenizer(several_txt_files_directory):
    assert universal_file_counter(several_txt_files_directory, "txt", str.split) == 10
