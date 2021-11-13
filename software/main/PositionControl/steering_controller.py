from dataclasses import dataclass
from typing import Optional

from unum import units

from ..Chassis import Chassis
from ..Odometry import Odometry, Position
from ..Regulators import Regulator
from ..Path import Line
from ..config import Configurable


class SteeringController(Configurable):
    @dataclass
    class Config:
        position_threshold: units.m
        angle_threshold: units.rad

    def __init__(self,
                 chassis: Chassis,
                 odometry: Odometry,
                 regulator: Regulator,
                 cfg: Config) -> None:
        self.cfg = cfg

        self._chassis = chassis
        self._odometry = odometry
        self._regulator = regulator

        self.__target: Optional[Position] = None

    def set_target(self, target: Position) -> None:
        self.__target = target
        self._regulator.set_target(target.rotation)

    def update(self) -> None:
        actual = self._odometry.position.rotation
        regulation: units.rad = self._regulator.compute(actual)

        new_velocity = self._chassis.velocity
        new_velocity.angular += regulation  # TODO: ошибка размерностей (rad/s + rad)

        self._chassis.set_velocity(new_velocity)

    @property
    def finished(self) -> bool:
        if self.__target is None:
            return False

        actual = self._odometry.position
        distance = Line(actual.translation, self.__target.translation).length
        rotation_error = abs(actual.rotation - self.__target.rotation)

        return distance < self.cfg.position_threshold \
                and rotation_error < self.cfg.angle_threshold
