from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import Dict

from . import ChassisWheels
from . import WheelsVelocity, Velocity, Kinematics
from ..Odometry import Odometry
from ..Drivers.Base import Motor
from ..Regulators import Regulator
from ..config import Configurable
from .. import mps


class Chassis(Configurable):
    class Direction(IntEnum):
        BACKWARD = -1
        FORWARD = 1

    @dataclass
    class Config:
        direction_map: Dict[Chassis.Direction, Motor.Direction]

    def __init__(self, wheels: ChassisWheels,
                 odometry: Odometry,
                 regulator: Regulator,
                 config: Chassis.Config) -> None:
        self.cfg = config

        self._wheels = wheels
        self._odometry = odometry
        self._regulator = regulator

        self._kinematics = Kinematics(self.cfg.kinematics)

        self.__velocity = Velocity(0, 0)

    def set_velocity(self, velocity: Velocity) -> None:
        self._regulator.set_target(velocity)

    def set_speed(self, side: ChassisWheels.Side, speed: mps) -> None:
        self._wheels[side].set_speed(speed)

    def set_speed_all(self, speed: mps):
        self._wheels.all.set_speed(speed)

    def update(self) -> None:
        self._wheels.all.update()
        self._odometry.update()

        actual_velocity = self.velocity
        regulation: Velocity = self._regulator.compute(actual_velocity)
        new_velocity = self.__velocity + regulation
        self._apply_velocity(new_velocity)

    def _apply_velocity(self, velocity: Velocity):
        self.__velocity = velocity

        wheels_velocity = self._kinematics.inverse(velocity)
        self._wheels.left.set_speed(wheels_velocity.left)
        self._wheels.right.set_speed(wheels_velocity.right)

    @property
    def velocity(self) -> Velocity:
        return self._kinematics.forward(self.wheels_velocity)

    @property
    def wheels_velocity(self) -> WheelsVelocity:
        return WheelsVelocity(self._wheels.left.speed, self._wheels.right.speed)
