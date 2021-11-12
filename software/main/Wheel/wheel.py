from unum import units

from ..config import Configurable
from ..Regulators import Regulator
from .. import mps
from . import WheelEncoder, WheelMotor


class Wheel(Configurable):
    def __init__(self,
                 motor: WheelMotor,
                 encoder: WheelEncoder,
                 regulator: Regulator) -> None:
        self.motor = motor
        self.encoder = encoder
        self.regulator = regulator

    def set_speed(self, speed: mps) -> None:
        self.regulator.set_target(speed)

    def update(self) -> None:
        actual_speed = self.encoder.get()
        regulation: mps = self.regulator.compute(actual_speed)

        new_speed = self.motor.speed + round(regulation.asNumber())
        self.motor.set_speed(new_speed)
