from ..Drivers.Base import Accelerometer

from . import Odometry, Position


class AccelerometerOdometry(Odometry):
    def __init__(self, accelerometer: Accelerometer) -> None:
        super().__init__()

        self._accelerometer = accelerometer

    def update(self) -> None:
        raise NotImplementedError

    def get(self) -> Position:
        raise NotImplementedError
