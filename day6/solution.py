from collections import Counter

CYCLE = 6


def tick(ages):
    new_ages = Counter()
    for age, count in ages.items():
        if age == 0:
            new_age = CYCLE
            new_ages[CYCLE + 2] += count
        else:
            new_age = age - 1
        new_ages[new_age] += count
    return new_ages


def main(starting_ages, days):
    day_counter = Counter(starting_ages)

    finished = _main(day_counter, days)

    return sum(finished[elt] for elt in finished)


def _main(age_counter, days):
    if days == 0:
        return age_counter

    next_ages = tick(age_counter)
    return _main(next_ages, days - 1)


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    ages = input_lines()[0].split(",")
    ages[-1] = ages[-1][0]
    ages = [int(age) for age in ages]
    answer = main(ages, 256)
    print(f"Answer: {answer}")
