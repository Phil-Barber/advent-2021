def main(input_grid):
    grid = to_grid(input_grid)

    costs = [[0 for _j in range(len(grid[0]))] for _i in range(len(grid))]

    recalculate = True
    func = right_or_down_costs
    while recalculate:
        costs, recalculate = func(grid, costs)
        func = right_or_down_costs if func == left_or_up_costs else left_or_up_costs
    return costs[-1][-1]


def to_grid(input_grid):
    initial_grid = [[int(char) for char in row] for row in input_grid]
    """
    grids = [previous_grid]
    for i in range(8):
        new_grid = [[(num + i) for num in row] for row in previous_grid]
        new_grid = [[num if num < 10 else num % 9 for num in row] for row in new_grid]
        grids.append(new_grid)
        previous_grid = new_grid
    """

    orig_height = len(initial_grid)
    orig_width = len(initial_grid[0])
    new_height = orig_height * 5
    new_width = orig_width * 5
    final_grid = [[0 for _j in range(new_width)] for _i in range(new_height)]
    for i in range(new_height):
        for j in range(new_width):
            mod_i = i % orig_height
            mod_j = j % orig_width
            initial_val = initial_grid[mod_i][mod_j]
            num_i = int((i - mod_i) / orig_height)
            num_j = int((j - mod_j) / orig_width)
            new_val = initial_val + num_i + num_j
            new_val = new_val if new_val < 10 else new_val % 9
            final_grid[i][j] = new_val

    return final_grid


def right_or_down_costs(grid, costs):
    recalculate = False
    for i, row in enumerate(grid):
        for j, risk_level in enumerate(row):
            possible_costs = []
            if (i > 0 or j > 0) and costs[i][j] != 0:
                possible_costs.append(costs[i][j])
            if i > 0:
                possible_costs.append(costs[i - 1][j] + risk_level)
            if j > 0:
                possible_costs.append(costs[i][j - 1] + risk_level)

            if possible_costs:
                new_cost = min(possible_costs)
                if new_cost != costs[i][j]:
                    costs[i][j] = new_cost
                    recalculate = True
    return costs, recalculate


def left_or_up_costs(grid, costs):
    recalculate = False
    for i, row in enumerate(grid):
        for j, risk_level in enumerate(row):
            possible_costs = [costs[i][j]]
            if i < len(grid) - 1:
                possible_costs.append(costs[i + 1][j] + risk_level)
            if j < len(grid[0]) - 1:
                possible_costs.append(costs[i][j + 1] + risk_level)

            new_cost = min(possible_costs)
            if new_cost != costs[i][j]:
                costs[i][j] = new_cost
                recalculate = True
    return costs, recalculate


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
