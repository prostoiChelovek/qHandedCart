from __future__ import annotations

import math
from typing import Tuple

from unum import units

from .point import Point, PointTpl

LineTpl = Tuple[PointTpl, PointTpl]


class Line:
    def __init__(self, a: Point, b: Point) -> None:
        self.a = a
        self.b = b

    @staticmethod
    def parse(d: LineTpl) -> Line:
        return Line(*map(Point.parse, d))

    @property
    def slope(self) -> float:
        delta = self.a - self.b

        if delta.x == 0:
            return math.inf

        return delta.y / delta.x

    @property
    def angle(self) -> units.rad:
        return math.atan(self.slope) * units.rad

    def __sub__(self, o: Line) -> Line:
        return Line(self.a - o.a, self.b - o.b)

    def __iter__(self):
        for x in (self.a, self.b):
            yield x

    def __eq__(self, o: Line) -> bool:
        return tuple(self) == tuple(o)

    def __str__(self) -> str:
        return f"{{{self.a} -- {self.b}}}"

    def __repr__(self) -> str:
        return self.__str__()
