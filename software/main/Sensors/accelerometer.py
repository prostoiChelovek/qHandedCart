from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Acceleration:
    x: float
    y: float
    z: float


class Accelerometer(ABC):
    @abstractmethod
    def get(self) -> Acceleration:
        pass
