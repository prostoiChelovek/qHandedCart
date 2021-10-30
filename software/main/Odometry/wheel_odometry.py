from dataclasses import dataclass

from ..Drivers.Base import Encoder, EncoderData
from ..Chassis import ChassisWheels
from . import Odometry, Position


class ChassisEncoders:
    @dataclass
    class Data:
        front_left: EncoderData
        front_right: EncoderData
        rear_left: EncoderData
        rear_right: EncoderData

    def __init__(self, wheels: ChassisWheels) -> None:
        self._encoders = list(map(lambda x: x.encoder, wheels))

    def get(self) -> Data:
        return ChassisEncoders.Data(*map(Encoder.get, self._encoders))


class WheelOdometry(Odometry):
    def __init__(self, wheels: ChassisWheels) -> None:
        super().__init__()

        self._encoders = ChassisEncoders(wheels)

    def update(self) -> None:
        raise NotImplementedError

    def get(self) -> Position:
        raise NotImplementedError
