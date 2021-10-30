from ..Drivers.Base import Motor, Encoder
from ..Regulators import Regulator


class Wheel:
    def __init__(self,
                 motor: Motor,
                 encoder: Encoder,
                 regulator: Regulator) -> None:
        self.motor = motor
        self.encoder = encoder
        self.regulator = regulator

    def set_speed(self, speed: int) -> None:
        self.regulator.set_target(speed)

    def set_direction(self, direction: Motor.Direction) -> None:
        self.motor.set_direction(direction)

    def stop(self) -> None:
        # TODO: вероятно, это не лучший вариант

        self.set_speed(0)
        self.motor.stop()

    def update(self) -> None:
        actual_speed = self.actual_speed
        regulation = self.regulator.compute(actual_speed)

        new_speed = self.motor.speed + round(regulation)
        self.motor.set_speed(new_speed)

    @property
    def actual_speed(self) -> float:
        encoder_data = self.encoder.get()

        return encoder_data.ticks / encoder_data.time_delta.total_seconds()
