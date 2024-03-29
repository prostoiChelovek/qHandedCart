from __future__ import annotations

from typing import Tuple

from unum import units

PointTpl = Tuple[units.m, units.m]


class Point:
    def __init__(self, x: units.m, y: units.m) -> None:
        self.x = x
        self.y = y

    @staticmethod
    def parse(tpl: PointTpl) -> Point:
        return Point(*tpl)

    def __sub__(self, o: Point) -> Point:
        return Point(self.x - o.x, self.y - o.y)

    def __iter__(self):
        for x in (self.x, self.y):
            yield x

    def __eq__(self, o: Point) -> bool:
        return tuple(self) == tuple(o)

    def __str__(self) -> str:
        return f"{{{self.x}, {self.y}}}"
