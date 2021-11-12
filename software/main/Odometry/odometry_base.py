from dataclasses import dataclass
from abc import ABC, abstractmethod

import unum.units as units

from ..Path import Point
from ..kinematics import Velocity


@dataclass
class Rotation:
    x: units.deg
    y: units.deg


@dataclass
class Position:
    translation: Point
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
