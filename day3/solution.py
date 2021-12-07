from collections import namedtuple
from collections.abc import Iterator


def lines() -> Iterator:
    with open("input") as input_file:
        yield from input_file.readlines()


def report(file_lines) -> Iterator:
    yield from ((n for n in line if n != "\n") for line in file_lines)


def calculate_most_common(input_list):
    return 1 if sum(int(i) for i in input_list) > len(input_list) / 2 else 0


if __name__ == "__main__":
    file_lines = lines()
    report_lines = report(file_lines)

    most_common = [calculate_most_common(i) for i in zip(*report_lines)]

    gamma = int("".join(str(b) for b in most_common), 2)
    epsilon = int("".join("0" if b else "1" for b in most_common), 2)
    print(most_common, gamma, epsilon)

    answer = gamma * epsilon
    print(f"Answer: {answer}")
