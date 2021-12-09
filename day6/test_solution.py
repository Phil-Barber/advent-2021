from collections import Counter

import pytest

import solution as s

example_ages = [3, 4, 3, 1, 2]


@pytest.mark.parametrize(
    "days, expected", ((0, len(example_ages)), (18, 26), (80, 5934))
)
def test_main(days, expected):
    ans = s.main(example_ages, days)
    assert ans == expected


def test__main():
    end = [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]
    assert s._main(Counter(example_ages), 18) == Counter(end)


@pytest.mark.parametrize(
    "ages, expected",
    (
        ([1, 2], [0, 1]),
        ([0, 1, 1, 2, 3, 2], [6, 0, 0, 1, 2, 1, 8]),
        ([0], [6, 8]),
        ([0, 0], [6, 6, 8, 8]),
        ([1, 0], [0, 6, 8]),
    ),
)
def test_tick(ages, expected):
    assert s.tick(Counter(ages)) == Counter(expected)
