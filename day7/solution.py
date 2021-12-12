import statistics


def triangle_num(number):
    return sum(num for num in range(number + 1))


def fuel_for_position(positions, move_to):
    return sum(triangle_num(int(abs(position - move_to))) for position in positions)


def find_best_position(positions):
    return statistics.median(positions)


def main(positions):
    low_pos, high_pos = min(positions), max(positions)
    costs = [
        fuel_for_position(positions, position) for position in range(low_pos, high_pos)
    ]
    return min(costs)


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    positions = input_lines()[0].split(",")
    positions[-1] = positions[-1][:-1]
    positions = [int(pos) for pos in positions]
    answer = main(positions)
    print(f"Answer: {answer}")
