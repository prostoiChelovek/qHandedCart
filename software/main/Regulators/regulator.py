from abc import ABC, abstractmethod

from ..config import Configurable


class Regulator(Configurable, ABC):
    @abstractmethod
    def set_target(self, target: float) -> None:
        pass

    @abstractmethod
    def compute(self, actual: float) -> float:
        pass
