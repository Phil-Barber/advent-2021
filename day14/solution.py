from collections import Counter


def main(inputs):
    template = inputs[0]
    mapping = parse_mapping(inputs[2:])

    template_counter, letter_counter = Counter(), Counter()
    for idx in range(len(template) - 1):
        template_counter[template[idx : idx + 2]] += 1
        letter_counter[template[idx]] += 1
    letter_counter[template[-1]] += 1

    for _ in range(40):
        new_counter = Counter()
        for pair in template_counter:
            n = template_counter[pair]
            result = mapping.get(pair, "")
            if result != "":
                new_counter[pair[0] + result] += n
                new_counter[result + pair[1]] += n
                letter_counter[result] += n
        template_counter = new_counter

    values = letter_counter.values()
    return max(values) - min(values)


def parse_mapping(mapping_lines):
    mappings = [mapping.split(" -> ") for mapping in mapping_lines]
    return {key: value for key, value in mappings}


def step(before, mapping):
    after = ""
    for idx in range(len(before) - 1):
        pair = before[idx : idx + 2]
        insert = mapping.get(pair, "")
        after += before[idx] + insert
    after += before[-1]
    return after


#####


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    inputs = [line[:-1] for line in inputs if line[0]]
    print(inputs[0])
    print(inputs[-1])
    answer = main(inputs)
    print(f"Answer: {answer}")
