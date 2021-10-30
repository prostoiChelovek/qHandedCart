from dataclasses import dataclass
from enum import IntEnum, Enum, auto

from ..Drivers.Base import Motor
from . import Wheel, SynchronizedWheels


@dataclass
class ChassisWheels:
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


class Chassis:
    class Direction(IntEnum):
        BACKWARD = -1
        FORWARD = 1

    def __init__(self, wheels: ChassisWheels) -> None:
        self.direction_map = {
                Chassis.Direction.FORWARD: Motor.Direction.CLOCKWISE,
                Chassis.Direction.BACKWARD: Motor.Direction.COUNTERCLOCKWISE,
                }

        self._wheels = wheels

    def stop(self, side: ChassisWheels.Side) -> None:
        self._wheels[side].stop()

    def set_speed(self, side: ChassisWheels.Side, speed: int) -> None:
        self._wheels[side].set_speed(speed)

    def set_direction(self, side: ChassisWheels.Side,
                      direction: Direction) -> None:
        real_direction = self.direction_map[direction]
        self._wheels[side].set_direction(real_direction)

    def stop_all(self) -> None:
        self._wheels.all.stop()

    def set_speed_all(self, speed: int):
        self._wheels.all.set_speed(speed)

    def set_direction_all(self, direction: Direction) -> None:
        real_direction = self.direction_map[direction]
        self._wheels.all.set_direction(real_direction)

    def update(self) -> None:
        self._wheels.all.update()
