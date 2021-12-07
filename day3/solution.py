def lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


def report(file_lines) -> list[list[int]]:
    return [[int(n) for n in line if n != "\n"] for line in file_lines]


def calculate_most_common(input_list, least=False):
    cmp = (lambda x, y: x < y) if least else (lambda x, y: x >= y)
    sum_vals = sum(i for i in input_list)
    half = len(input_list) / 2
    return 1 if cmp(sum_vals, half) else 0


def get_filtered_values(values, filter_key, idx):
    if len(values) > 1:
        values = list(filter(lambda arr: arr[idx] == filter_key, values))
    return values


def recursive_group_by(entries, idx):
    gamma_values, epsilon_values = entries

    if idx == len(gamma_values[0]):
        return gamma_values[0], epsilon_values[0]

    gamma_filter = calculate_most_common(list(zip(*gamma_values))[idx])
    epsilon_filter = calculate_most_common(list(zip(*epsilon_values))[idx], least=True)

    print(gamma_values[:3])
    print(epsilon_values[:3])
    print(gamma_filter, epsilon_filter, idx)
    gamma_values = get_filtered_values(gamma_values, gamma_filter, idx)
    epsilon_values = get_filtered_values(epsilon_values, epsilon_filter, idx)

    return recursive_group_by((gamma_values, epsilon_values), idx + 1)


def arr_to_int(arr):
    return int("".join(str(n) for n in arr), 2)


if __name__ == "__main__":
    file_lines = lines()
    report_lines = report(file_lines)

    gamma, epsilon = recursive_group_by((report_lines, report_lines), 0)
    print(gamma)
    print(epsilon)

    answer = arr_to_int(gamma) * arr_to_int(epsilon)
    print(f"Answer: {answer}")
