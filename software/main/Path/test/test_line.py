import math

from .. import Point, Line


def test_parse():
    tpl = ((1, 2), (3, 4))
    assert Line.parse(tpl) == Line(Point(1, 2), Point(3, 4))


def test_slope():
    slopes = [
            (Line.parse(((0, 0), (1, 1))), 1),
            (Line.parse(((0, 0), (2, 2))), 1),
            (Line.parse(((0, 0), (1, 2))), 2),
            (Line.parse(((0, 0), (2, 1))), 0.5),
            (Line.parse(((1, 1), (0, 0))), 1),
            (Line.parse(((1, 1), (0, 0))), 1),
            ]

    for line, slope in slopes:
        assert line.slope == slope


def test_slope_vertical():
    line = Line.parse(((0, 0), (0, 1)))
    assert line.slope == math.inf
