from abc import ABC, abstractmethod
from enum import IntEnum


class Motor(ABC):
    class Direction(IntEnum):
        COUNTERCLOCKWISE = -1
        CLOCKWISE = 1

    def __init__(self) -> None:
        super().__init__()

        self._speed = 0

    def set_speed(self, speed: int) -> None:
        speed_capped = max(0, min(speed, 100))
        self._speed = speed_capped
        self._set_speed(speed_capped)

    @property
    def speed(self) -> int:
        return self._speed

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def set_direction(self, direction: Direction) -> None:
        pass

    @abstractmethod
    def _set_speed(self, speed: int) -> None:
        pass
