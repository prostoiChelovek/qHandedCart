from __future__ import annotations

from dataclasses import dataclass

from unum import units

from .. import mps, radps
from ..config import Configurable

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


class KinematicsBase(Configurable):
    @dataclass
    class Config:
        wheel_radius: units.m
        base_length: units.m

    def __init__(self, cfg: KinematicsBase.Config) -> None:
        super().__init__()

        self.cfg = cfg


class Forward(KinematicsBase):
    def velocity(self, velocities: WheelsVelocity) -> Velocity:
        return Velocity(
                linear = (self.cfg.wheel_radius / 2) * velocities.sum,
                angular = (self.cfg.wheel_radius / self.cfg.base_length) * velocities.diff
                )


class Inverse(KinematicsBase):
    def wheel_velocities(self, velocity: Velocity) -> WheelsVelocity:
        return WheelsVelocity(
                right = self._calc(velocity, 1),
                left = self._calc(velocity, -1),
                )
    
    def _calc(self, velocity: Velocity, sign: int) -> mps:
        return (2 * velocity.linear + (sign * velocity.angular * self.cfg.base_length)) \
             / (2 * self.cfg.wheel_radius)
