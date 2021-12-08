from collections import Counter

import pytest

import solution as s

example_lines = (
    ((0, 9), (5, 9)),
    ((8, 0), (0, 8)),
    ((9, 4), (3, 4)),
    ((2, 2), (2, 1)),
    ((7, 0), (7, 4)),
    ((6, 4), (2, 0)),
    ((0, 9), (2, 9)),
    ((3, 4), (1, 4)),
    ((0, 0), (8, 8)),
    ((5, 5), (8, 2)),
)

example_grid = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
]


def test_parse_input_lines():
    input_lines = [
        "0,9 -> 5,9\n",
        "8,0 -> 0,8\n",
        "9,4 -> 3,4\n",
        "2,2 -> 2,1\n",
        "7,0 -> 7,4\n",
        "6,4 -> 2,0\n",
        "0,9 -> 2,9\n",
        "3,4 -> 1,4\n",
        "0,0 -> 8,8\n",
        "5,5 -> 8,2\n",
    ]
    assert tuple(s.parse_input(input_lines)) == example_lines


def test_main():
    assert s.main(example_lines) == 5


def test_counter_danger():
    example_dict = {
        (x, y): value
        for y, row in enumerate(example_grid)
        for x, value in enumerate(row)
    }
    counter = Counter(example_dict)
    assert s.counter_danger(counter) == 5


@pytest.mark.parametrize(
    "line_coords, expected",
    (
        (((2, 2), (2, 4)), ((2, 2), (2, 3), (2, 4))),
        (((2, 4), (2, 2)), ((2, 4), (2, 3), (2, 2))),
        (((2, 1), (4, 1)), ((2, 1), (3, 1), (4, 1))),
        (((1, 1), (3, 3)), ((1, 1), (2, 2), (3, 3))),
        (((3, 3), (1, 1)), ((3, 3), (2, 2), (1, 1))),
    ),
)
def test_get_full_line(line_coords, expected):
    assert tuple(s.get_full_line(line_coords)) == expected
