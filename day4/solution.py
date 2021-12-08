import dataclasses

BOARD_SIZE = 5


@dataclasses.dataclass
class Board:
    rows: list[list[int]]
    called: list[list[int]] = dataclasses.field(
        default_factory=lambda: [
            [0 for _i in range(BOARD_SIZE)] for _j in range(BOARD_SIZE)
        ]
    )

    def __repr__(self):
        return "rows:\n".join(str(row) + "\n" for row in self.rows)

    def call(self, number):
        for y, row in enumerate(self.rows):
            for x, value in enumerate(row):
                if value == number:
                    self.called[y][x] = 1
                    return

    def has_won(self):
        winning = [1 for _ in range(BOARD_SIZE)]
        for row in self.called + list(zip(*self.called)):
            if list(row) == winning:
                return True
        return False

    def sum(self):
        return sum(
            value
            for y, row in enumerate(self.rows)
            for x, value in enumerate(row)
            if not self.called[y][x]
        )


def call_numbers(boards, calls):
    for call_number in calls:
        for board in boards:
            board.call(call_number)
            if board.has_won():
                return board, call_number


def bingo(number_calls, boards_input):
    boards = [Board(rows=rows) for rows in boards_input]

    board, winning_call = call_numbers(boards, number_calls)

    return board.sum() * winning_call


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


def parse_input():
    lines = input_lines()
    number_calls = [int(number) for number in lines[0].split(",")]
    board_lines = [
        lines[i : i + BOARD_SIZE] for i in range(2, len(lines), BOARD_SIZE + 1)
    ]
    boards = [
        [
            [int(value) for value in row.split(" ") if value and value != "\n"]
            for row in board_line
        ]
        for board_line in board_lines
    ]
    return number_calls, boards


if __name__ == "__main__":
    number_calls, boards = parse_input()
    answer = bingo(number_calls, boards)
    print(f"Answer: {answer}")
