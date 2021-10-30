from typing import Iterable

from ..Drivers.Base import Motor


class SynchronizedMotors(Motor):
    def __init__(self, motors: Iterable[Motor]) -> None:
        self._motors = motors

    def stop(self) -> None:
        for m in self._motors:
            m.stop()

    def set_direction(self, direction: Motor.Direction) -> None:
        for m in self._motors:
            m.set_direction(direction)

    def _set_speed(self, speed: int) -> None:
        for m in self._motors:
            m._set_speed(speed)
