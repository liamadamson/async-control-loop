from async_control_loop import input
from unittest.mock import Mock
import pytest
import freezegun


@pytest.mark.parametrize("name", ["name1", "input"])
def test_name(name):
    test_input = input.Input(name)
    assert test_input.name == name


def test_name_is_optional():
    test_input = input.Input()


class FakeInput(input.Input):
    def __init__(self, mock: Mock) -> None:
        super().__init__()
        self._mock = mock

    def _concrete_update(self) -> float:
        return self._mock.update()


def test_update_calls_concrete_update():
    mock = Mock()
    test_input = FakeInput(mock)

    mock.update.assert_not_called()
    test_input.update()
    mock.update.assert_called_once()


def test_initial_time_last_updated_is_none():
    test_input = FakeInput(Mock())
    assert test_input.time_last_updated is None


@pytest.mark.parametrize("freezetime, unix_time", [
    ("2023-01-29 09:00:00", 1674982800),
    ("2025-01-01 14:00:00", 1735740000),
])
def test_time_last_updated_is_updated(freezetime, unix_time):
    with freezegun.freeze_time(freezetime):
        test_input = FakeInput(Mock())
        test_input.update()
        assert test_input.time_last_updated == unix_time


def test_initial_read_returns_none():
    test_input = FakeInput(Mock())
    assert test_input.read() is None


def test_read_returns_correct_value():
    sensor = Mock()
    sensor.update.return_value = 3.14

    test_input = FakeInput(sensor)
    test_input.update()

    assert test_input.read() == 3.14