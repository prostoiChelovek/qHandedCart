from __future__ import annotations

from typing import Tuple

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
        return (self.a.x - self.b.x) / (self.a.y - self.b.y)
