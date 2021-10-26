from .. import Point


def test_parse():
    tpl = (3, 14)
    assert Point.parse(tpl) == Point(3, 14)
