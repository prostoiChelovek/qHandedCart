from __future__ import annotations

from dataclasses import dataclass

from unum import units

from ..Drivers.Base import Motor


class WheelMotor:
    @dataclass
    class Config:
        max_speed: units.m / units.s

    def __init__(self, motor: Motor, cfg: WheelMotor.Config) -> None:
        self.cfg = cfg

        self._motor = motor

    def set_speed(self, speed: units.m / units.s) -> None:
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
    def speed(self) -> units.m / units.s:
        return  self.cfg.max_speed / 100 * self._motor.speed
