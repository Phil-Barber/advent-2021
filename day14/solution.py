from collections import Counter


def main(inputs):
    template = inputs[0]
    mapping = parse_mapping(inputs[2:])

    for _ in range(10):
        template = step(template, mapping)

    counts = Counter(template).values()
    return max(counts) - min(counts)


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
