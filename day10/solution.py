import statistics
from collections import deque

matching = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def main(lines):
    scores = [chunk_score(chunk) for chunk in lines]
    non_zero = [score for score in scores if score != 0]
    return statistics.median(non_zero)


def chunk_score(chunk):
    stack = deque()
    for char in chunk:
        if char in matching.values():
            stack.append(char)
        else:
            if stack[-1] == matching[char]:
                stack.pop()
            else:
                return 0
    if len(stack) == 0:
        return 0

    score = 0
    while len(stack):
        score *= 5
        score += scores[stack.pop()]
    return score


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
