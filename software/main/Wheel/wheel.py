from unum import units

from ..config import Configurable
from ..Regulators import Regulator
from . import WheelEncoder, WheelMotor


class Wheel(Configurable):
    def __init__(self,
                 motor: WheelMotor,
                 encoder: WheelEncoder,
                 regulator: Regulator) -> None:
        self.motor = motor
        self.encoder = encoder
        self.regulator = regulator

    def set_speed(self, speed: units.m / units.s) -> None:
        self.regulator.set_target(speed)

    def stop(self) -> None:
        # TODO: вероятно, это не лучший вариант

        self.set_speed(0)

    def update(self) -> None:
        actual_speed = self.encoder.get()
        regulation: (units.m / units.s) = self.regulator.compute(actual_speed)

        new_speed = self.motor.speed + round(regulation.asNumber())
        self.motor.set_speed(new_speed)
