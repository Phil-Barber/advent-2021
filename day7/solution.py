import statistics


def main(positions):
    median = statistics.median(positions)
    return sum(abs(position - median) for position in positions)


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    positions = input_lines()[0].split(",")
    print(positions)
    positions[-1] = positions[-1][:-1]
    positions = [int(pos) for pos in positions]
    print(positions)
    answer = main(positions)
    print(f"Answer: {answer}")
