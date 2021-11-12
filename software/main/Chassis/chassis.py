from __future__ import annotations

from . import ChassisWheels
from ..kinematics import WheelsVelocity, Velocity, Kinematics
from ..Odometry import Odometry
from ..Regulators import Regulator
from ..config import Configurable


class Chassis(Configurable):
    def __init__(self,
                 wheels: ChassisWheels,
                 odometry: Odometry,
                 regulator: Regulator,
                 kinematics: Kinematics) -> None:
        self._wheels = wheels
        self._odometry = odometry
        self._regulator = regulator
        self._kinematics = kinematics

        self.__velocity = Velocity(0, 0)

    def set_velocity(self, velocity: Velocity) -> None:
        self._regulator.set_target(velocity)

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
