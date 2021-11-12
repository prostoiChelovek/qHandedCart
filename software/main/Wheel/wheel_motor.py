from __future__ import annotations

from dataclasses import dataclass

from unum import units

from ..Drivers.Base import Motor
from .. import mps


class WheelMotor:
    @dataclass
    class Config:
        max_speed: mps

    def __init__(self, motor: Motor, cfg: WheelMotor.Config) -> None:
        self.cfg = cfg

        self._motor = motor

        self.__speed: mps = 0

    def set_speed(self, speed: mps) -> None:
        self.__speed = speed

        if speed < 0:
            self._motor.set_direction(Motor.Direction.COUNTERCLOCKWISE)
        elif speed > 0:
            self._motor.set_direction(Motor.Direction.CLOCKWISE)
        else:
            self._motor.stop()
            return

        percent = round(abs(speed) / self.cfg.max_speed * 100)
        self._motor.set_speed(percent)

    @property
    def speed(self) -> mps:
        # TODO: значение верно токльо если мотором никто больше не управляет
        return self.__speed
