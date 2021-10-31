from . import Regulator


class Pid(Regulator):
    def __init__(self, p, i, d):
        self.i = i
        self.p = p
        self.d = d

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

        return self.p * e \
             + self.i * self._Ie \
             + self.d * de

    def __str__(self) -> str:
        params = f"P: {self.p}, I: {self.i}, D: {self.d}"
        state = f"target: {self._target}, last_error: {self._last_error}, Ie: {self._Ie}"
        return f"PID: {{\n\t{params}\n\t{state}\n}}"
