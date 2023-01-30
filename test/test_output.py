from async_control_loop import output
from unittest.mock import Mock
import pytest
import freezegun


@pytest.mark.parametrize("name", ["output1, output2"])
def test_output_name(name):
    test_output = output.Output(name)
    assert test_output.name == name


def test_default_name():
    test_output = output.Output()
    assert test_output.name is None


class MockOutput(output.Output):

    def __init__(self, mock) -> None:
        super().__init__()
        self._mock = mock

    def _concrete_write(self, data = None):
        self._mock.write(data)


def test_write_calls_concrete_write():
    mock = Mock()
    test_output = MockOutput(mock)

    mock.write.assert_not_called()
    test_output.write("123")
    mock.write.assert_called_once()
    mock.write.assert_called_with("123")


def test_default_time_last_written():
    test_output = MockOutput(Mock())
    assert test_output.time_last_written is None


@pytest.mark.parametrize("freezetime, unix_time", [
    ("2023-01-29 09:00:00", 1674982800),
    ("2025-01-01 14:00:00", 1735740000),
])
def test_write_updates_time_last_read(freezetime, unix_time):
    with freezegun.freeze_time(freezetime, unix_time):
            test_output = MockOutput(Mock())
            test_output.write("123")
            assert test_output.time_last_written == unix_time


def test_last_written_value_initially_none():
    test_output = MockOutput(Mock())
    assert test_output.last_written_value is None


def test_last_written_value_is_update():
    mock = Mock()
    test_output = MockOutput(Mock())

    test_output.write("123")
    assert test_output.last_written_value == "123"