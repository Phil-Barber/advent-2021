import pytest

import solution as s


@pytest.mark.parametrize(
    "positions, expected",
    (
        ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 37),
        ([10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0], 70),
    ),
)
def test_main(positions, expected):
    assert s.main(positions) == expected
