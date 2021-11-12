from typing import Iterable

from . import Wheel
from .. import mps


class SynchronizedWheels:
    def __init__(self, motors: Iterable[Wheel]) -> None:
        self._wheels = motors

    def set_speed(self, speed: mps) -> None:
        for w in self._wheels:
            w.set_speed(speed)

    def update(self) -> None:
        for w in self._wheels:
            w.update()

    @property
    def speed(self) -> mps:
        speeds = list(map(lambda x: x.speed, self._wheels))
        return sum(speeds, 0 * mps) / len(speeds)
