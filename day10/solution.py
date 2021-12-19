from collections import deque

matching = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def main(lines):
    return sum(chunk_score(line) for line in lines)


def chunk_score(chunk):
    stack = deque()
    for char in chunk:
        print("".join(stack), char)
        if char in matching.values():
            stack.append(char)
        else:
            if stack[-1] == matching[char]:
                stack.pop()
            else:
                return scores[char]
    return 0


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
