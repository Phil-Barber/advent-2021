from collections import Counter
from itertools import chain


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


def parse_input(input_lines):
    drop_newline = [line[:-1] for line in input_lines]
    joint_coord_strings = (line.split(" -> ") for line in drop_newline)

    coord_strings = (
        (tuple(coord1.split(",")), tuple(coord2.split(",")))
        for coord1, coord2 in joint_coord_strings
    )
    return (
        (
            tuple(int(coord) for coord in coords[0]),
            tuple(int(coord) for coord in coords[1]),
        )
        for coords in coord_strings
    )


class Vertical:
    pass


def get_full_line(line_coords):
    coord1, coord2 = line_coords
    x1, y1, x2, y2 = coord1 + coord2
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx if dx != 0 else Vertical

    if m is Vertical:
        y_step = 1 if y2 > y1 else -1
        return ((x1, y) for y in range(y1, y2 + y_step, y_step))
    c = y1 - m * x1
    x_step = 1 if x2 > x1 else -1
    return ((x, int(m * x + c)) for x in range(x1, x2 + x_step, x_step))


def counter_danger(counter):
    return sum(1 for elt in counter if counter[elt] > 1)


def main(lines):
    non_diaganol = (
        line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]
    )
    line_coords = chain.from_iterable(get_full_line(line) for line in non_diaganol)
    coord_counter = Counter(line_coords)
    return counter_danger(coord_counter)


if __name__ == "__main__":
    lines = parse_input(input_lines())
    answer = main(lines)
    print(f"Answer: {answer}")
