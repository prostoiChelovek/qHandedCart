from typing import Iterable 

from . import Odometry, Position


class CombinedOdometry(Odometry):
    def __init__(self, providers: Iterable[Odometry]) -> None:
        super().__init__()

        self._providers = providers

    def update(self) -> None:
        for p in self._providers:
            p.update()

    def get(self) -> Position:
        postiions = map(Odometry.get, self._providers)
        raise NotImplementedError
