import pytest

import solution as s

test_input = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581",
]

test_answer = 315


"""
input_up = [  # it's possible to go UP
    "19111",
    "11191",
    "99991",
]
up_answer = 8

input_left = [  # it's possible to go LEFT
    "119",
    "919",
    "119",
    "199",
    "111",
]
left_answer = 8
"""


@pytest.mark.parametrize(
    "input_grid, answer",
    (
        (test_input, test_answer),
        # (input_up, up_answer),
        # (input_left, left_answer),
    ),
)
def test_main(input_grid, answer):
    assert s.main(input_grid) == answer
