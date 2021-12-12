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
    "inputs, outputs",
    (
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
            {"be": 1, "cgeb": 4, "edb": 7, "cfbegad": 8},
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
            {"gc": 1, "gfec": 4, "cbg": 7, "gcadebf": 8},
        ),
    ),
)
def test_decipher_inputs(inputs, outputs):
    assert s.decipher_inputs(inputs) == outputs


@pytest.mark.parametrize(
    "codex, outputs, expected",
    (
        (
            {"be": 1, "cgeb": 4, "edb": 7, "cfbegad": 8},
            ("fdgacbe", "cefdb", "cefbgd", "gcbe"),
            2,
        ),
        (
            {"gc": 1, "gfec": 4, "cbg": 7, "gcadebf": 8},
            ("fcgedb", "cgb", "dgebacf", "gc"),
            3,
        ),
    ),
)
def test_count_ouputs(codex, outputs, expected):
    assert s.count_outputs(codex, outputs) == expected


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
