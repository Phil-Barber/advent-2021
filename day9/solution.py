def main(lines):
    grid = [list(map(lambda n: int(n), iter(row))) for row in lines]
    low_points = get_low_points(grid)
    return sum([grid[y][x] + 1 for x, y in low_points])


def get_low_points(grid):
    return [
        (x, y)
        for y, row in enumerate(grid)
        for x, cell in enumerate(row)
        if is_low_point(x, y, grid)
    ]


def is_low_point(*args):
    funcs = (is_lt_left, is_lt_right, is_lt_up, is_lt_down)
    return all(func(*args) for func in funcs)


def is_lt_left(x, y, grid):
    return x == 0 or grid[y][x - 1] > grid[y][x]


def is_lt_right(x, y, grid):
    return x == len(grid[y]) - 1 or grid[y][x + 1] > grid[y][x]


def is_lt_up(x, y, grid):
    return y == 0 or grid[y - 1][x] > grid[y][x]


def is_lt_down(x, y, grid):
    return y == len(grid) - 1 or grid[y + 1][x] > grid[y][x]


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    inputs = [line[:-1] for line in inputs if line[0]]
    print(inputs[-1])
    answer = main(inputs)
    print(f"Answer: {answer}")
