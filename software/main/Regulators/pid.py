from dataclasses import dataclass

from . import Regulator


class Pid(Regulator):
    @dataclass
    class Config:
        p: float = 1
        i: float = 1
        d: float = 1

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg

        self._target = 0

        self._last_error = 0
        self._Ie = 0

    def set_target(self, target: float) -> None:
        # TODO: is this enough?
        self._target = target

    def compute(self, actual: float) -> float:
        e = self._target - actual

        de = e - self._last_error
        self._Ie += e
        self._last_error = e

        return self.cfg.p * e \
             + self.cfg.i * self._Ie \
             + self.cfg.d * de

    def __str__(self) -> str:
        params = f"P: {self.p}, I: {self.i}, D: {self.d}"
        state = f"target: {self._target}, last_error: {self._last_error}, Ie: {self._Ie}"
        return f"PID: {{\n\t{params}\n\t{state}\n}}"
