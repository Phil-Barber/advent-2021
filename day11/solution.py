import contextlib
import dataclasses


@dataclasses.dataclass
class Octopus:
    level: int
    flashes: int = 0
    has_flashed: bool = False

    def can_flash(self):
        return self.level > 9 and not self.has_flashed


def main(energy_levels):
    octopuses = [[Octopus(int(level)) for level in row] for row in energy_levels]

    step_count = 0
    while not all_flashed(octopuses):
        octopuses = step(octopuses)
        step_count += 1

    return step_count


def step(octopuses):
    incremented = increment(octopuses)

    while can_flash(incremented):
        incremented = flash(incremented)

    reset = reset_level_and_has_flashed(incremented)
    return reset


def increment(octopuses):
    return [
        [dataclasses.replace(octopus, level=octopus.level + 1) for octopus in row]
        for row in octopuses
    ]


def can_flash(octopuses):
    return any(octopus.can_flash() for row in octopuses for octopus in row)


def flash(octopuses):
    new_octopuses = [
        [dataclasses.replace(octopus) for octopus in row] for row in octopuses
    ]
    for y, row in enumerate(new_octopuses):
        for x, octopus in enumerate(row):
            if octopus.can_flash():
                octopus.has_flashed = True
                new_octopuses[y][x].flashes += 1
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= y + i < len(new_octopuses) and 0 <= x + j < len(row):
                            new_octopuses[y + i][x + j].level += 1
    return new_octopuses


def reset_level_and_has_flashed(octopuses):
    return [
        [
            dataclasses.replace(octopus, level=0, has_flashed=False)
            if octopus.has_flashed
            else dataclasses.replace(octopus)
            for octopus in row
        ]
        for row in octopuses
    ]


def all_flashed(octopuses):
    return all(octopus.level == 0 for row in octopuses for octopus in row)


def print_octs(octopuses):
    print("~~~")
    for row in octopuses:
        print(row)


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
