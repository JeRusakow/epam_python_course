import random
from unittest.mock import patch

from homework4.task3.task_3_get_print_output import my_precious_logger


@patch("sys.stdout.write")
@patch("sys.stderr.write")
def test_stderr_write(fake_stderr, fake_stdout):
    message = "error: Some Error"
    my_precious_logger(message)
    fake_stderr.assert_called_once_with(message)
    fake_stdout.not_called()


@patch("sys.stdout.write")
@patch("sys.stderr.write")
def test_stdout_write(fake_stderr, fake_stdout):
    message = "hooray: No error!"
    my_precious_logger(message)
    fake_stdout.assert_called_once_with(message)
    fake_stderr.assert_not_called()


@patch("sys.stderr.write")
@patch("sys.stdout.write")
def test_std_write_random_text(fake_stdout, fake_stderr):
    """
    Generates a random message to be logged. Test assumes that generated string must not be logged.
    Probability of generating a message which starts with 'error' and therefore should be logged is 4.2E-10.
    This means that mean time to fail is approximately 1.9 billion runs.
    """
    message = "".join([chr(random.randint(48, 123)) for i in range(10)])
    my_precious_logger(message)

    fake_stdout.assert_called_once_with(message)
    fake_stderr.assert_not_called()
