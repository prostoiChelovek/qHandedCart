import pytest

from .. import Point, Line, Path


@pytest.fixture
def path():
    return Path([Point(1, 2), Point(3, 4), Point(5, 6)])


def test_parse(path):
    d = [ (1, 2), (3, 4), (5, 6) ]
    assert Path.parse(d) == path


def test_iter(path):
    i = iter(path)
    assert next(i) == Line.parse(((1, 2), (3, 4)))
    assert next(i) == Line.parse(((3, 4), (5, 6)))
    with pytest.raises(StopIteration):
        next(i)


def test_iter_empty():
    path = Path([])
    with pytest.raises(StopIteration):
        next(iter(path))


def test_iter_single_node():
    path = Path([Point(0, 0)])
    with pytest.raises(StopIteration):
        next(iter(path))
