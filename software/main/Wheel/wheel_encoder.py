from __future__ import annotations

from dataclasses import dataclass
import math

from unum import units

from ..config import Configurable
from ..Drivers.Base import Encoder


class WheelEncoder(Configurable):
    @dataclass
    class Config:
        num_gaps: int
        wheel_radius: units.m

    def __init__(self, encoder: Encoder, cfg: WheelEncoder.Config) -> None:
        self.cfg = cfg

        self._encoder = encoder

    def get(self) -> units.m / units.s:
        encoder_data = self._encoder.get()
        linear_distance = encoder_data.ticks * self.pulses_per_m
        return linear_distance / encoder_data.seconds

    @property
    def arc_length(self) -> units.m:
        return 2 * math.pi * self.cfg.wheel_radius
    
    @property
    def pulses_per_m(self) -> (1 / units.m):
        return self.cfg.num_gaps / self.arc_length
