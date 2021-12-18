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

basins = [
    [(1, 0), (0, 0), (0, 1)],
    [(5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (6, 1), (8, 1), (9, 1), (9, 2)],
    [
        (2, 1),
        (3, 1),
        (4, 1),
        (1, 2),
        (2, 2),
        (3, 2),
        (4, 2),
        (5, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
        (4, 3),
        (1, 4),
    ],
    [(7, 2), (6, 3), (7, 3), (8, 3), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4)],
]


def test_main():
    assert s.main(example) == 1134


def test_get_low_points():
    assert s.get_low_points(grid) == low_points


@pytest.mark.parametrize("low_point", low_points)
def test_is_low_point(low_point):
    assert s.is_low_point(*low_point, grid)


@pytest.mark.parametrize("low_point, basin", zip(low_points, basins))
def test_get_basin(low_point, basin):
    assert set(s.get_basin(*low_point, grid)) == set(basin)
