from abc import ABC, abstractmethod


class Regulator(ABC):
    @abstractmethod
    def set_target(self, target: float) -> None:
        pass

    @abstractmethod
    def compute(self, actual: float) -> float:
        pass
