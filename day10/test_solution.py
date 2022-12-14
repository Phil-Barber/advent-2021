import pytest

import solution as s


@pytest.mark.parametrize(
    "chunk, score",
    (
        ("()", 0),
        ("[]", 0),
        ("{}", 0),
        ("<>", 0),
        ("<)", 0),
        ("[}", 0),
        ("{()()()}", 0),
        ("{()()()}<[]>", 0),
        ("{()()()<[]>]", 0),
        ("{(]()()}", 0),
        ("<([{}])>", 0),
        ("[<>({}){}[([])<>]]", 0),
        ("[<>{}){}([])<>]]", 0),
        ("(((((((((())))))))))", 0),
        ("((((>((((())))))))))", 0),
        ("[({(<(())[]>[[{[]{<()<>>", 288957),
        ("[(()[<>])]({[<{<<[]>>(", 5566),
        ("(((({<>}<{<{<>}{[]{[]{}", 1480781),
        ("{<[[]]>}<{[{[{[]{()[[[]", 995444),
        ("<{([{{}}[<[[[<>{}]]]>[]]", 294),
    ),
)
def test_chunk_score(chunk, score):
    assert s.chunk_score(chunk) == score


example = [
    "[<>({}){}[([])<>]]",
    "[<>{}){}([])<>]]",
    "(((((((((())))))))))",
    "((((>((((())))))))))",
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "(((({<>}<{<{<>}{[]{[]{}",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def test_main():
    assert s.main(example) == 288957
