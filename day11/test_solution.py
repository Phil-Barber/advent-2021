import pytest

import solution as s

energy_levels = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]


def test_main():
    assert s.main(energy_levels, 100) == 1656


@pytest.mark.parametrize(
    "octopuses, new_octopuses",
    (
        ([[s.Octopus(9)]], [[s.Octopus(0, 1)]]),
        ([[s.Octopus(8), s.Octopus(9, 1)]], [[s.Octopus(0, 1), s.Octopus(0, 2)]]),
        (
            [
                [s.Octopus(9), s.Octopus(7, 1), s.Octopus(9)],
                [s.Octopus(3), s.Octopus(4), s.Octopus(4)],
            ],
            [
                [s.Octopus(0, 1), s.Octopus(0, 2), s.Octopus(0, 1)],
                [s.Octopus(6), s.Octopus(8), s.Octopus(7)],
            ],
        ),
    ),
)
def test_step(octopuses, new_octopuses):
    assert s.step(octopuses) == new_octopuses


@pytest.mark.parametrize(
    "octopuses, new_octopuses",
    (
        ([[s.Octopus(9)]], [[s.Octopus(10)]]),
        ([[s.Octopus(8), s.Octopus(9, 1)]], [[s.Octopus(9), s.Octopus(10, 1)]]),
        (
            [
                [s.Octopus(9), s.Octopus(7, 1), s.Octopus(9)],
                [s.Octopus(3), s.Octopus(4), s.Octopus(4)],
            ],
            [
                [s.Octopus(10), s.Octopus(8, 1), s.Octopus(10)],
                [s.Octopus(4), s.Octopus(5), s.Octopus(5)],
            ],
        ),
    ),
)
def test_increment(octopuses, new_octopuses):
    assert s.increment(octopuses), new_octopuses


@pytest.mark.parametrize(
    "octopuses, can_flash",
    (
        ([[s.Octopus(5)]], False),
        ([[s.Octopus(10)]], True),
        ([[s.Octopus(10, 0, has_flashed=True)]], False),
        ([[s.Octopus(9), s.Octopus(10, 1)]], True),
        ([[s.Octopus(4), s.Octopus(7, 1)], [s.Octopus(4), s.Octopus(10)]], True),
    ),
)
def test_can_flash(octopuses, can_flash):
    assert s.can_flash(octopuses) == can_flash
