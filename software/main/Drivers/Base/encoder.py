from datetime import timedelta
from dataclasses import dataclass
from abc import ABC, abstractmethod

from unum import units


@dataclass
class EncoderData:
    ticks: int
    time_delta: timedelta

    @property
    def seconds(self) -> units.s:
        return self.time_delta.total_seconds() * units.s


class Encoder(ABC):
    @abstractmethod
    def get(self) -> EncoderData:
        pass
