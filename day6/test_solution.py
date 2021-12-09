import pytest

import solution as s

example_ages = [3, 4, 3, 1, 2]


@pytest.mark.parametrize(
    "days, expected", ((0, len(example_ages)), (18, 26), (80, 5934))
)
def test_main(days, expected):
    assert s.main(example_ages, days) == expected


@pytest.mark.parametrize(
    "ages, expected",
    (
        ([1, 2], [0, 1]),
        ([0], [6, 8]),
        ([1, 0], [0, 6, 8]),
    ),
)
def test_tick(ages, expected):
    assert s.tick(ages) == expected
