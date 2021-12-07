import pytest

import solution as s


class TestCalculateMostCommon:
    @pytest.mark.parametrize(
        "input_list, least, expected",
        (
            ([0, 0, 0], False, 0),
            ([0, 0, 0], True, 1),
            ([0, 1, 1], False, 1),
            ([0, 1, 1], True, 0),
            ([0, 1, 1, 0], False, 1),
            ([0, 1, 1, 0], True, 0),
        ),
    )
    def test_caclulates_most_common(self, input_list, least, expected):
        assert s.calculate_most_common(input_list, least) == expected
