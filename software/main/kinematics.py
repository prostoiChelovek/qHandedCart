from __future__ import annotations

from dataclasses import dataclass

from unum import units

from . import mps, radps
from .config import Configurable

# based on https://youtu.be/aE7RQNhwnPQ

@dataclass
class WheelsVelocity:
    left: mps
    right: mps

    @property
    def sum(self) -> mps:
        return self.right + self.left

    @property
    def diff(self) -> mps:
        return self.right - self.left


@dataclass
class Velocity:
    linear: mps
    angular: radps

    def __neg__(self) -> Velocity:
        return Velocity(-self.linear, -self.angular)

    def __add__(self, o: Velocity) -> Velocity:
        return Velocity(self.linear + o.angular, self.angular + o.angular)
    __iadd__ = __add__

    def __sub__(self, o: Velocity) -> Velocity:
        return self + (-o)
    __isub__ = __sub__

    def __mul__(self, o: float) -> Velocity:
        return Velocity(self.linear * o, self.angular * o)
    __rmul__ = __mul__


class Kinematics(Configurable):
    @dataclass
    class Config:
        wheel_radius: units.m
        base_length: units.m

    def __init__(self, cfg: Kinematics.Config) -> None:
        super().__init__()

        self.cfg = cfg

    def forward(self, velocities: WheelsVelocity) -> Velocity:
        return Velocity(
                linear = (self.cfg.wheel_radius / 2) * velocities.sum,
                angular = (self.cfg.wheel_radius / self.cfg.base_length) * velocities.diff
                )

    def inverse(self, velocity: Velocity) -> WheelsVelocity:
        return WheelsVelocity(
                right = self.__inverse_calc(velocity, 1),
                left = self.__inverse_calc(velocity, -1),
                )
    
    def __inverse_calc(self, velocity: Velocity, sign: int) -> mps:
        return (2 * velocity.linear + (sign * velocity.angular * self.cfg.base_length)) \
             / (2 * self.cfg.wheel_radius)
