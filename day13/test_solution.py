import pytest

import solution as s

test_input = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5",
]


def test_main():
    s.main(test_input) == 17


@pytest.mark.parametrize(
    "dot, index, fold_value, expected",
    (
        ((8, 4), 0, 7, (6, 4)),
        ((9, 4), 0, 7, (5, 4)),
        ((9, 4), 1, 3, (9, 2)),
    ),
)
def test_fold_dot(dot, index, fold_value, expected):
    assert s.fold_dot(dot, index, fold_value) == expected
