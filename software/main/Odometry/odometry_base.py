from dataclasses import dataclass
from abc import ABC, abstractmethod

import unum.units as units


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

    @abstractmethod
    def get(self) -> Position:
        pass
