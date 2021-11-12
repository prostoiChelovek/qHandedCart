from typing import Iterable

from . import Wheel


class SynchronizedWheels:
    def __init__(self, motors: Iterable[Wheel]) -> None:
        self._wheels = motors

    def set_speed(self, speed: int) -> None:
        for w in self._wheels:
            w.set_speed(speed)

    def update(self) -> None:
        for w in self._wheels:
            w.update()
