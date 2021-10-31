from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum
from typing import Dict

from . import ChassisWheels
from ..Odometry import Odometry
from ..Drivers.Base import Motor


class Chassis:
    class Direction(IntEnum):
        BACKWARD = -1
        FORWARD = 1

    @dataclass
    class Config:
        direction_map: Dict[Chassis.Direction, Motor.Direction]

    def __init__(self, wheels: ChassisWheels, odometry: Odometry, config: Chassis.Config) -> None:
        self.cfg = config

        self._wheels = wheels
        self._odometry = odometry

    def stop(self, side: ChassisWheels.Side) -> None:
        self._wheels[side].stop()

    def set_speed(self, side: ChassisWheels.Side, speed: int) -> None:
        self._wheels[side].set_speed(speed)

    def set_direction(self, side: ChassisWheels.Side,
                      direction: Direction) -> None:
        real_direction = self.cfg.direction_map[direction]
        self._wheels[side].set_direction(real_direction)

    def stop_all(self) -> None:
        self._wheels.all.stop()

    def set_speed_all(self, speed: int):
        self._wheels.all.set_speed(speed)

    def set_direction_all(self, direction: Direction) -> None:
        real_direction = self.cfg.direction_map[direction]
        self._wheels.all.set_direction(real_direction)

    def update(self) -> None:
        self._wheels.all.update()
        self._odometry.update()
