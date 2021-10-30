from numbers import Real
from abc import ABC, abstractmethod


class Regulator(ABC):
    @abstractmethod
    def set_target(self, target: Real) -> None:
        pass

    @abstractmethod
    def compute(self, actual: Real) -> Real:
        pass
