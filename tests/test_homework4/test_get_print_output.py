from unittest.mock import patch

from homework4.task3.task_3_get_print_output import my_precious_logger


@patch("sys.stderr.write")
def test_stderr_write(fake_stderr):
    message = "error: Some Error"
    my_precious_logger(message)
    assert fake_stderr.called_once_with(message)


@patch("sys.stdout.write")
def test_stdout_write(fake_stdout):
    message = "hooray: No error!"
    my_precious_logger(message)
    assert fake_stdout.called_once_with(message)
