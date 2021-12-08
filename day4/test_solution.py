import solution as s

number_calls = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]

board1 = [
    [22, 13, 17, 11, 0],
    [8, 2, 23, 4, 24],
    [21, 9, 14, 16, 7],
    [6, 10, 3, 18, 5],
    [1, 12, 20, 15, 19],
]
board2 = [
    [3, 15, 0, 2, 22],
    [9, 18, 13, 17, 5],
    [19, 8, 7, 25, 23],
    [20, 11, 10, 24, 4],
    [14, 21, 16, 12, 6],
]

board3 = [
    [14, 21, 17, 24, 4],
    [10, 16, 15, 9, 19],
    [18, 8, 23, 26, 20],
    [22, 11, 13, 6, 5],
    [2, 0, 12, 3, 7],
]


def test_main_example_input():
    assert s.bingo(number_calls, [board1, board2, board3]) == 1924


def test_board_call_sets_called_number():
    board = s.Board(rows=board1)
    board.call(16)
    assert board.called == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_board_call_does_not_unset_previous_calls():
    called = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    board = s.Board(rows=board1, called=called)
    board.call(10)
    expected = called
    expected[2][1] = 1
    assert board.called == expected


def test_board_has_won_true_if_horizontal_win():
    called = [
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
    ]
    board = s.Board(rows=board1, called=called)
    assert board.has_won()


def test_board_has_won_true_if_vertical_win():
    called = [
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0],
    ]
    board = s.Board(rows=board1, called=called)
    assert board.has_won()


def test_board_has_won_false_if_not_won():
    called = [
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    board = s.Board(rows=board1, called=called)
    assert not board.has_won()


def test_call_numbers_returns_losing_board_and_number():
    boards = [s.Board(rows=board) for board in (board1, board2, board3)]
    board, num = s.call_numbers(boards, number_calls)
    assert board == boards[1]
    assert num == 13


def test_sums_only_not_called_numbers():
    rows = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    called = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ]
    assert s.Board(rows=rows, called=called).sum() == 4
