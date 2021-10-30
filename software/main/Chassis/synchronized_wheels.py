from typing import Iterable

from ..Drivers.Base import Motor
from . import Wheel


class SynchronizedWheels:
    def __init__(self, motors: Iterable[Wheel]) -> None:
        self._wheels = motors

    def stop(self) -> None:
        for w in self._wheels:
            w.stop()

    def set_direction(self, direction: Motor.Direction) -> None:
        for w in self._wheels:
            w.set_direction(direction)

    def set_speed(self, speed: int) -> None:
        for w in self._wheels:
            w.set_speed(speed)

    def update(self) -> None:
        for w in self._wheels:
            w.update()
