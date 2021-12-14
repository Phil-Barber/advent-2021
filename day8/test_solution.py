import pytest

import solution as s

example = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]


def test_main():
    assert s.main(example) == 26


@pytest.mark.parametrize(
    "inputs, possibilities",
    (
        (
            (
                "acedgfb",
                "cdfbe",
                "gcdfa",
                "fbcad",
                "dab",
                "cefabd",
                "cdfgeb",
                "eafb",
                "cagedb",
                "ab",
            ),
            [
                {"cefabd", "cdfgeb", "cagedb"},
                {"ab"},
                {"cdfbe", "gcdfa", "fbcad"},
                {"cdfbe", "gcdfa", "fbcad"},
                {"eafb"},
                {"cdfbe", "gcdfa", "fbcad"},
                {"cefabd", "cdfgeb", "cagedb"},
                {"dab"},
                {"acedgfb"},
                {"cefabd", "cdfgeb", "cagedb"},
            ],
        ),
    ),
)
def test_build_possibilities(inputs, possibilities):
    assert s.build_possibilities(inputs) == possibilities


@pytest.mark.parametrize(
    "possibilities, numbers",
    (
        (
            [
                {"cefabd", "cdfgeb", "cagedb"},
                {"ab"},
                {"cdfbe", "gcdfa", "fbcad"},
                {"cdfbe", "gcdfa", "fbcad"},
                {"eafb"},
                {"cdfbe", "gcdfa", "fbcad"},
                {"cefabd", "cdfgeb", "cagedb"},
                {"dab"},
                {"acedgfb"},
                {"cefabd", "cdfgeb", "cagedb"},
            ],
            [
                "cagedb",
                "ab",
                "gcdfa",
                "fbcad",
                "eafb",
                "cdfbe",
                "cdfgeb",
                "dab",
                "acedgfb",
                "cefabd",
            ],
        ),
    ),
)
def test_get_numbers(possibilities, numbers):
    assert s.get_numbers(possibilities) == numbers


@pytest.mark.parametrize(
    "codex, outputs, expected",
    (
        (
            [
                "cagedb",
                "ab",
                "gcdfa",
                "fbcad",
                "eafb",
                "cdfbe",
                "cdfgeb",
                "dab",
                "acedgfb",
                "cefabd",
            ],
            ("cdfeb", "fcadb", "cdfeb", "cdbaf"),
            5353,
        ),
    ),
)
def test_deciphered_outputs(codex, outputs, expected):
    assert s.deciphered_outputs(codex, outputs) == expected


def test_parse_input():
    assert s.parse_input(example) == [
        (
            (
                "be",
                "cfbegad",
                "cbdgef",
                "fgaecd",
                "cgeb",
                "fdcge",
                "agebfd",
                "fecdb",
                "fabcd",
                "edb",
            ),
            ("fdgacbe", "cefdb", "cefbgd", "gcbe"),
        ),
        (
            (
                "edbfga",
                "begcd",
                "cbg",
                "gc",
                "gcadebf",
                "fbgde",
                "acbgfd",
                "abcde",
                "gfcbed",
                "gfec",
            ),
            ("fcgedb", "cgb", "dgebacf", "gc"),
        ),
        (
            (
                "fgaebd",
                "cg",
                "bdaec",
                "gdafb",
                "agbcfd",
                "gdcbef",
                "bgcad",
                "gfac",
                "gcb",
                "cdgabef",
            ),
            ("cg", "cg", "fdcagb", "cbg"),
        ),
        (
            (
                "fbegcd",
                "cbd",
                "adcefb",
                "dageb",
                "afcb",
                "bc",
                "aefdc",
                "ecdab",
                "fgdeca",
                "fcdbega",
            ),
            ("efabcd", "cedba", "gadfec", "cb"),
        ),
        (
            (
                "aecbfdg",
                "fbg",
                "gf",
                "bafeg",
                "dbefa",
                "fcge",
                "gcbea",
                "fcaegb",
                "dgceab",
                "fcbdga",
            ),
            ("gecf", "egdcabf", "bgf", "bfgea"),
        ),
        (
            (
                "fgeab",
                "ca",
                "afcebg",
                "bdacfeg",
                "cfaedg",
                "gcfdb",
                "baec",
                "bfadeg",
                "bafgc",
                "acf",
            ),
            ("gebdcfa", "ecba", "ca", "fadegcb"),
        ),
        (
            (
                "dbcfg",
                "fgd",
                "bdegcaf",
                "fgec",
                "aegbdf",
                "ecdfab",
                "fbedc",
                "dacgb",
                "gdcebf",
                "gf",
            ),
            ("cefg", "dcbef", "fcge", "gbcadfe"),
        ),
        (
            (
                "bdfegc",
                "cbegaf",
                "gecbf",
                "dfcage",
                "bdacg",
                "ed",
                "bedf",
                "ced",
                "adcbefg",
                "gebcd",
            ),
            ("ed", "bcgafe", "cdgba", "cbgef"),
        ),
        (
            (
                "egadfb",
                "cdbfeg",
                "cegd",
                "fecab",
                "cgb",
                "gbdefca",
                "cg",
                "fgcdab",
                "egfdb",
                "bfceg",
            ),
            ("gbdfcae", "bgc", "cg", "cgb"),
        ),
        (
            (
                "gcafb",
                "gcf",
                "dcaebfg",
                "ecagb",
                "gf",
                "abcdeg",
                "gaef",
                "cafbge",
                "fdbac",
                "fegbdc",
            ),
            ("fgae", "cfgab", "fg", "bagce"),
        ),
    ]
