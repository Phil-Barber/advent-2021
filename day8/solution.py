# array positions represent positions on the display
board_positions = {
    0: [1, 1, 1, 0, 1, 1, 1],
    1: [0, 0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 1, 1, 0, 1],
    3: [1, 0, 1, 1, 0, 1, 1],
    4: [0, 1, 1, 1, 0, 1, 0],
    5: [1, 1, 0, 1, 0, 1, 1],
    6: [1, 1, 0, 1, 1, 1, 1],
    7: [1, 0, 1, 0, 0, 1, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1],
}


def main(lines):
    parsed_lines = parse_input(lines)

    count = 0
    for inputs, outputs in parsed_lines:
        possibilities = build_possibilities(inputs)
        board = reduce_possibilities(possibilities)
        deciphered = deciphered_outputs(board, outputs)
        count += deciphered
    return count


def parse_input(lines):
    parsed = []
    for line in lines:
        input_string, output_string = line.split(" | ")
        inputs = tuple(input_string.split(" "))
        outputs = tuple(output_string.split(" "))
        parsed.append((inputs, outputs))
    return parsed


def build_possibilities(inputs):
    possibilities = [set() for _ in range(10)]
    for digit in inputs:
        possible_numbers = (
            number
            for number, position in board_positions.items()
            if len(digit) == sum(position)
        )
        for possibility in possible_numbers:
            possibilities[possibility].add(digit)
    return possibilities


def get_numbers(possibilities):
    def is_subset(d_num, segments, is_subset_of_segments):
        idx_where_1 = [seg for seg, is_on in enumerate(segments) if is_on == 1]
        parent_matches = [is_subset_of_segments[seg] == 1 for seg in idx_where_1]
        return all(parent_matches)

    combinations = []
    for number in range(10):
        this_num = board_positions[number]
        numbers_contained_in_number = [
            d_num
            for d_num, segments in board_positions.items()
            if is_subset(d_num, segments, this_num)
        ]
        print(number, numbers_contained_in_number)
        one_of = possibilities[number]

        found = False
        for contained in numbers_contained_in_number:
            if len(one_of) == 1:
                break
            one_of = { option for option in one_of if 
        combinations.append(one_of.pop())
    return combinations  




def deciphered_outputs(codex, outputs):
    deciphered_sets = tuple((set(deciphered) for deciphered in codex.keys()))
    return sum(1 for digit in outputs if set(digit) in deciphered_sets)


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    print(inputs[-1])
    inputs = [line[:-1] for line in inputs if line[0]]
    print(inputs[-1])
    answer = main(inputs)
    print(f"Answer: {answer}")
