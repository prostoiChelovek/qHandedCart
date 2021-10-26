from dataclasses import dataclass
from enum import IntEnum, Enum, auto

from . import Motor
from . import SynchronizedMotors


@dataclass
class ChassisMotors:
    class Side(Enum):
        LEFT = auto()
        RIGHT = auto()

    front_left: Motor
    front_right: Motor
    rear_left: Motor
    rear_right: Motor

    @property
    def left(self) -> SynchronizedMotors:
        return SynchronizedMotors((self.front_left, self.rear_left))

    @property
    def right(self) -> SynchronizedMotors:
        return SynchronizedMotors((self.front_right, self.rear_right))

    @property
    def front(self) -> SynchronizedMotors:
        return SynchronizedMotors((self.front_left, self.front_right))

    @property
    def rear(self) -> SynchronizedMotors:
        return SynchronizedMotors((self.rear_left, self.rear_right))

    @property
    def all(self) -> SynchronizedMotors:
        return SynchronizedMotors(tuple(self))

    def __getitem__(self, side: Side) -> SynchronizedMotors:
        return {
                ChassisMotors.Side.LEFT: self.left,
                ChassisMotors.Side.RIGHT: self.right,
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

    def __init__(self, motors: ChassisMotors) -> None:
        self.direction_map = {
                Chassis.Direction.FORWARD: Motor.Direction.CLOCKWISE,
                Chassis.Direction.BACKWARD: Motor.Direction.COUNTERCLOCKWISE,
                }

        self._motors = motors

    def stop(self, side: ChassisMotors.Side) -> None:
        self._motors[side].stop()

    def set_speed(self, side: ChassisMotors.Side, speed: int) -> None:
        self._motors[side].set_speed(speed)

    def set_direction(self, side: ChassisMotors.Side,
                      direction: Direction) -> None:
        motor_direction = self.direction_map[direction]
        self._motors[side].set_direction(motor_direction)

    def stop_all(self) -> None:
        self._motors.all.stop()

    def set_speed_all(self, speed: int):
        self._motors.all.set_speed(speed)

    def set_direction_all(self, direction: Direction) -> None:
        motor_direction = self.direction_map[direction]
        self._motors.all.set_direction(motor_direction)
