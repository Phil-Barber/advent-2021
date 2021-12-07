from collections import namedtuple
from collections.abc import Iterator

Submarine = namedtuple("Submarine", ("hoz", "depth", "aim"))


def lines() -> Iterator:
    with open("input") as input_file:
        yield from input_file.readlines()


def commands(file_lines) -> Iterator:
    yield from (line.split(" ") for line in file_lines)


def move_submarine(submarine, cmd, qty):
    if cmd == "forward":
        return Submarine(
            submarine.hoz + qty,
            submarine.depth * submarine.aim,
            submarine.aim,
        )
    if cmd == "down":
        return Submarine(submarine.hoz, submarine.depth, submarine.aim + qty)
    if cmd == "up":
        return Submarine(submarine.hoz, submarine.depth, submarine.aim - qty)
    raise Exception(f"InvalidCommand: {cmd=}")


if __name__ == "__main__":
    file_lines = lines()
    submarine = Submarine(0, 0, 0)

    for cmd, qty in commands(file_lines):
        submarine = move_submarine(submarine, cmd, int(qty))

    answer = submarine.depth * submarine.hoz
    print(f"Answer: {answer}")
