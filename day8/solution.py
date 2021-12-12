def main(lines):
    parsed_lines = parse_input(lines)

    count = 0
    for inputs, outputs in parsed_lines:
        codex = decipher_inputs(inputs)
        deciphered = count_outputs(codex, outputs)
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


def decipher_inputs(inputs):
    codex = {}
    for digit in inputs:
        deciphered = decipher_digit(digit)
        if deciphered:
            codex[digit] = deciphered
    return codex


def decipher_digit(digit):
    if len(digit) == 2:
        return 1
    if len(digit) == 4:
        return 4
    if len(digit) == 3:
        return 7
    if len(digit) == 7:
        return 8
    return None


def count_outputs(codex, outputs):
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
