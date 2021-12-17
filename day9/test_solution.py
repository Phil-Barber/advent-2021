import pytest

import solution as s

example = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]

grid = [list(map(lambda n: int(n), iter(row))) for row in example]

low_points = [(1, 0), (9, 0), (2, 2), (6, 4)]


def test_main():
    assert s.main(example) == 15


def test_get_low_points():
    assert s.get_low_points(grid) == low_points


@pytest.mark.parametrize("low_point", low_points)
def test_is_low_point(low_point):
    assert s.is_low_point(*low_point, grid)
