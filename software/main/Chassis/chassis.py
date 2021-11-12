from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import Dict

from . import ChassisWheels
from ..Odometry import Odometry
from ..Drivers.Base import Motor
from ..config import Configurable
from .. import mps


class Chassis(Configurable):
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


    def set_speed(self, side: ChassisWheels.Side, speed: mps) -> None:
        self._wheels[side].set_speed(speed)

    def set_speed_all(self, speed: mps):
        self._wheels.all.set_speed(speed)

    def update(self) -> None:
        self._wheels.all.update()
        self._odometry.update()
