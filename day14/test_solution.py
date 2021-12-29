import pytest

import solution as s

mapping_lines = [
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]

mapping = {
    "CH": "B",
    "HH": "N",
    "CB": "H",
    "NH": "C",
    "HB": "C",
    "HC": "B",
    "HN": "C",
    "NN": "C",
    "BH": "H",
    "NC": "B",
    "NB": "B",
    "BN": "B",
    "BB": "N",
    "BC": "B",
    "CC": "N",
    "CN": "C",
}


def test_main():
    input = ["NNCB", "", *mapping_lines]
    assert s.main(input) == 1588


@pytest.mark.parametrize(
    "before, after",
    (
        ("NNCB", "NCNBCHB"),
        ("NCNBCHB", "NBCCNBBBCBHCB"),
        ("NBCCNBBBCBHCB", "NBBBCNCCNBBNBNBBCHBHHBCHB"),
        (
            "NBBBCNCCNBBNBNBBCHBHHBCHB",
            "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB",
        ),
    ),
)
def test_step(before, after):
    assert s.step(before, mapping) == after


def test_parse_mapping():
    s.parse_mapping(mapping_lines) == mapping
