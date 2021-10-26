from __future__ import annotations

from typing import Tuple

PointTpl = Tuple[int, int]


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    @staticmethod
    def parse(tpl: PointTpl) -> Point:
        return Point(*tpl)

    def __str__(self) -> str:
        return f"{{{self.x}, {self.y}}}"
