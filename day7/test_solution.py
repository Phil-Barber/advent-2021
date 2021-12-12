import pytest

import solution as s

example_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


@pytest.mark.parametrize(
    "positions, move_to, expected",
    (
        (example_positions, 2, 206),
        (example_positions, 5, 168),
    ),
)
def test_fuel_for_position(positions, move_to, expected):
    assert s.fuel_for_position(positions, move_to) == expected


@pytest.mark.parametrize("number, expected", ((1, 1), (2, 3), (3, 6), (4, 10)))
def test_triangle(number, expected):
    assert s.triangle_num(number) == expected


def test_main():
    assert s.main(example_positions) == 168
