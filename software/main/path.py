from __future__ import annotations

from itertools import islice

from typing import List

from .point import Point, PointTpl
from .line import Line


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    "https://stackoverflow.com/a/6822773/9577873"
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


class Path:
    def __init__(self, nodes: List[Point]) -> None:
        self._nodes = nodes

    @staticmethod
    def parse(d: List[PointTpl]) -> Path:
        return Path(list(map(Point.parse, d)))

    def __iter__(self):
        return map(lambda x: Line(*x), window(self._nodes, 2))
