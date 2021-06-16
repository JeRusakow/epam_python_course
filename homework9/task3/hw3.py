"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(  # noqa: CCR001
    dir_path: Path,
    file_extension: str,
    tokenizer: Optional[Callable] = None,
    recursive=False,
) -> int:
    """
    This functions takes directory path and file extension and counts all the lines or
    tokens, if tokenizer is specified.

    Args:
        dir_path: Path to dir
        file_extension: Extension of files to count lines or tokens within
        tokenizer: [optional] A Callable to split string into tokens
        recursive: whether to perform recursive search across all subdirectories

    Returns:
        Amount of strings (or tokens) across all the files with given extension within
            specified directory
    """
    if not dir_path.exists():
        raise FileNotFoundError(f"Path '{dir_path}' does not exists")

    file_pattern = "**/*" if recursive else "*"

    file_list = dir_path.glob(f"{file_pattern}.{file_extension}")

    token_counter = 0

    for file in file_list:
        if not file.suffix == f".{file_extension}":
            continue

        with open(file) as f:
            for line in f:
                tokens = 1

                if tokenizer is not None:
                    tokens = len(tokenizer(line))

                token_counter += tokens

    return token_counter
