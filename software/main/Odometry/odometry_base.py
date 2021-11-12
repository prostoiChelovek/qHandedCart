from dataclasses import dataclass
from abc import ABC, abstractmethod

import unum.units as units

from ..kinematics import Velocity


@dataclass
class Translation:
    x: units.m
    y: units.m
    z: units.m


@dataclass
class Rotation:
    x: units.deg
    y: units.deg
    z: units.deg


@dataclass
class Position:
    translation: Translation
    rotation: Rotation


class Odometry(ABC):
    @abstractmethod
    def update(self) -> None:
        pass

    @property
    @abstractmethod
    def position(self) -> Position:
        pass

    @property
    @abstractmethod
    def velocity(self) -> Velocity:
        pass
