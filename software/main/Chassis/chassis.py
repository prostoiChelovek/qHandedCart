from typing import Callable, Tuple
from dataclasses import dataclass
from enum import IntEnum, Enum, auto

from . import Motor

MotorsPair = Tuple[Motor, Motor]


@dataclass
class ChassisMotors:
    front_left: Motor
    front_right: Motor
    rear_left: Motor
    rear_right: Motor

    @property
    def left(self) -> MotorsPair:
        return (self.front_left, self.rear_left)

    @property
    def right(self) -> MotorsPair:
        return (self.front_right, self.rear_right)

    @property
    def front(self) -> MotorsPair:
        return (self.front_left, self.front_right)

    @property
    def rear(self) -> MotorsPair:
        return (self.rear_left, self.rear_right)

    def __iter__(self):
        for x in (
                self.front_left,
                self.front_right,
                self.rear_left,
                self.rear_right
        ):
            yield x


class Chassis:
    class Side(Enum):
        LEFT = auto()
        RIGHT = auto()

    class Direction(IntEnum):
        BACKWARD = -1
        FORWARD = 1

    def __init__(self, motors: ChassisMotors) -> None:
        self.direction_map = {
                Chassis.Direction.FORWARD: Motor.Direction.CLOCKWISE,
                Chassis.Direction.BACKWARD: Motor.Direction.COUNTERCLOCKWISE,
                }

        self._motors = motors

    def stop(self, side: Side) -> None:
        self._call_on_side(side, Motor.stop)

    def set_speed(self, side: Side, speed: int) -> None:
        self._call_on_side(side, Motor.set_speed, speed)

    def set_direction(self, side: Side, direction: Direction) -> None:
        motor_direction = self.direction_map[direction]
        self._call_on_side(side, Motor.set_direction, motor_direction)

    def stop_all(self) -> None:
        self._call_on_all(Motor.stop)

    def set_speed_all(self, speed: int):
        self._call_on_all(Motor.set_speed, speed)

    def set_direction_all(self, direction: Direction) -> None:
        motor_direction = self.direction_map[direction]
        self._call_on_all(Motor.set_direction, motor_direction)

    def _get_side_motors(self, side: Side) -> MotorsPair:
        return {
                Chassis.Side.LEFT: self._motors.left,
                Chassis.Side.RIGHT: self._motors.right,
            }[side]

    def _call_on_side(self, side: Side, method: Callable,
                      *args, **kwargs) -> None:
        for m in self._get_side_motors(side):
            method(m, *args, **kwargs)

    def _call_on_all(self, method: Callable,
                     *args, **kwargs) -> None:
        for m in self._motors:
            method(m, *args, **kwargs)
