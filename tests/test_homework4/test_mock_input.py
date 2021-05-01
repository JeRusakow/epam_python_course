from unittest.mock import patch
from urllib.error import URLError

from pytest import raises

from homework4.task2.task_2_mock_input import count_dots_on_i


class FakeHTTPResponse:
    def __init__(self, status, body):
        self.status = status
        self.body = body

    def read(self):
        return self.body


@patch("urllib.request.urlopen")
def test_normal_execution(fake_urlopen):
    fake_urlopen.return_value = FakeHTTPResponse(200, b"This is fake content")
    assert count_dots_on_i("https://fake.adr") == 2


@patch("urllib.request.urlopen")
def test_status_not_ok(fake_urlopen):
    fake_urlopen.return_value = FakeHTTPResponse(404, "This is fake content")

    with raises(ValueError, match="Bad response code: 404"):
        count_dots_on_i("https://fake.adr")


@patch("urllib.request.urlopen")
def test_url_error(fake_urlopen):
    fake_urlopen.side_effect = URLError("Some URL error")

    with raises(ValueError, match="Unreachable https://fake.adr"):
        count_dots_on_i("https://fake.adr")
