CYCLE = 6


def tick(ages):
    new_ages = []
    for fish_age in ages:
        if fish_age == 0:
            new_ages.append(CYCLE)
            new_ages.append(CYCLE + 2)
        else:
            new_ages.append(fish_age - 1)
    return new_ages


def main(starting_ages, days):
    if days == 0:
        return len(starting_ages)

    next_ages = tick(starting_ages)
    return main(next_ages, days - 1)


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    ages = input_lines()[0].split(",")
    ages[-1] = ages[-1][0]
    ages = [int(age) for age in ages]
    answer = main(ages, 80)
    print(f"Answer: {answer}")
