import abc
import time
from typing import Optional, Generic, TypeVar


T = TypeVar('T')

class Output(Generic[T]):

    def __init__(self, name: Optional[str] =  None) -> None:
        self._name = name
        self._time_last_written: Optional[float] = None
        self._last_written_value: Optional[T] = None

    def write(self, data: T) -> None:
        self._concrete_write(data)
        self._time_last_written = time.time()
        self._last_written_value = data

    @property
    def name(self) -> Optional[str]:
        return self._name

    @property
    def time_last_written(self) -> Optional[float]:
        return self._time_last_written

    @property
    def last_written_value(self) -> Optional[T]:
        return self._last_written_value

    @abc.abstractmethod
    def _concrete_write(self, data: T) -> None:
        ...
