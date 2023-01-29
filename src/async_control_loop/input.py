import abc
import time
from typing import Optional, Generic, TypeVar


T = TypeVar('T')


class Input(Generic[T]):

    def __init__(self, name: Optional[str] = None) -> None:
        self._name = name

        self._current_value: Optional[T] = None
        self._time_last_updated: Optional[float] = None

    def update(self) -> None:
        self._current_value = self._concrete_update()
        self._time_last_updated = time.time()

    def read(self) -> Optional[T]:
        return self._current_value

    @abc.abstractmethod
    def _concrete_update(self) -> T:
        ...

    @property
    def name(self) -> Optional[str]:
        return self._name

    @property
    def time_last_updated(self) -> Optional[float]:
        return self._time_last_updated
