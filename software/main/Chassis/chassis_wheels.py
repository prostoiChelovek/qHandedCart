from dataclasses import dataclass
from enum import Enum, auto

from . import Wheel, SynchronizedWheels
from ..config import Configurable


@dataclass
class ChassisWheels(Configurable):
    class Side(Enum):
        LEFT = auto()
        RIGHT = auto()

    front_left: Wheel
    front_right: Wheel
    rear_left: Wheel
    rear_right: Wheel

    @property
    def left(self) -> SynchronizedWheels:
        return SynchronizedWheels((self.front_left, self.rear_left))

    @property
    def right(self) -> SynchronizedWheels:
        return SynchronizedWheels((self.front_right, self.rear_right))

    @property
    def front(self) -> SynchronizedWheels:
        return SynchronizedWheels((self.front_left, self.front_right))

    @property
    def rear(self) -> SynchronizedWheels:
        return SynchronizedWheels((self.rear_left, self.rear_right))

    @property
    def all(self) -> SynchronizedWheels:
        return SynchronizedWheels(tuple(self))

    def __getitem__(self, side: Side) -> SynchronizedWheels:
        return {
                ChassisWheels.Side.LEFT: self.left,
                ChassisWheels.Side.RIGHT: self.right,
            }[side]

    def __iter__(self):
        for x in (
                self.front_left,
                self.front_right,
                self.rear_left,
                self.rear_right
        ):
            yield x


