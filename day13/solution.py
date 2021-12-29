import matplotlib.pyplot as plt


def dots_and_folds(inputs):
    split_point = inputs.index("")

    dots_strings = [dot.split(",") for dot in inputs[:split_point]]
    dots = set((int(x), int(y)) for x, y in dots_strings)

    fold_strings = [
        instruction.split(" ")[-1] for instruction in inputs[split_point + 1 :]
    ]
    folds = [instruction.split("=") for instruction in fold_strings]

    return dots, folds


def main(inputs):
    dots, folds = dots_and_folds(inputs)

    for fold in folds:
        dots = perform_fold(dots, fold)

    return dots


def perform_fold(dots, fold):
    new_dots = set()
    for dot in dots:
        index = 0 if fold[0] == "x" else 1

        if dot[index] > int(fold[1]):
            new_dot = fold_dot(dot, index, int(fold[1]))
            new_dots.add(new_dot)
        else:
            new_dots.add(dot)
    return new_dots


def fold_dot(dot, index, fold_value):
    diff = dot[index] - fold_value
    new_idx = dot[index] - 2 * (diff)

    other_pos = int(not index)
    new_dot = [0, 0]
    new_dot[index] = new_idx
    new_dot[other_pos] = dot[other_pos]
    new_dot = tuple(new_dot)
    return new_dot


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
    for x, y in answer:
        plt.plot(x, -y, "bo")
    plt.show()
