from datetime import timedelta
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class EncoderData:
    ticks: int
    time_delta: timedelta


class Encoder(ABC):
    @abstractmethod
    def get(self) -> EncoderData:
        pass
