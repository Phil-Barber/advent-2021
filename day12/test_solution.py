import pytest

import solution as s

example1 = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
]


example2 = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]

example3 = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW",
]


@pytest.mark.parametrize(
    "edges, num_paths",
    (
        (example1, 10),
        (example2, 19),
        (example3, 226),
    ),
)
def test_get_num_paths_from_edges(edges, num_paths):
    assert s.get_num_paths_from_edges(edges) == num_paths


class TestNode:
    def test_is_large(self):
        assert not s.Node("avc").is_large
        assert s.Node("HSD").is_large

    def test_is_start(self):
        assert not s.Node("end").is_start
        assert s.Node("start").is_start

    def test_is_end(self):
        assert not s.Node("start").is_end
        assert s.Node("end").is_end


class TestEdge:
    @pytest.mark.parametrize(
        "string, edge",
        (
            (
                "start-A",
                s.Edge({s.Node("start"), s.Node("A")}),
            ),
            ("end-a", s.Edge({s.Node("end"), s.Node("a")})),
        ),
    )
    def test_from_string(self, string, edge):
        assert s.Edge.from_string(string) == edge


@pytest.mark.parametrize(
    "edges, paths",
    (
        (
            [s.Edge.from_string(edge) for edge in example1],
            [
                [
                    s.Node("start"),
                    s.Node("A"),
                    s.Node("c"),
                    s.Node("A"),
                    s.Node("b"),
                    s.Node("A"),
                    s.Node("end"),
                ],
                [
                    s.Node("start"),
                    s.Node("A"),
                    s.Node("c"),
                    s.Node("A"),
                    s.Node("b"),
                    s.Node("end"),
                ],
                [s.Node("start"), s.Node("A"), s.Node("c"), s.Node("A"), s.Node("end")],
                [
                    s.Node("start"),
                    s.Node("A"),
                    s.Node("b"),
                    s.Node("A"),
                    s.Node("c"),
                    s.Node("A"),
                    s.Node("end"),
                ],
                [s.Node("start"), s.Node("A"), s.Node("b"), s.Node("A"), s.Node("end")],
                [s.Node("start"), s.Node("A"), s.Node("b"), s.Node("end")],
                [s.Node("start"), s.Node("A"), s.Node("end")],
                [
                    s.Node("start"),
                    s.Node("b"),
                    s.Node("A"),
                    s.Node("c"),
                    s.Node("A"),
                    s.Node("end"),
                ],
                [s.Node("start"), s.Node("b"), s.Node("A"), s.Node("end")],
                [s.Node("start"), s.Node("b"), s.Node("end")],
            ],
        ),
        (
            [s.Edge({s.Node("start"), s.Node("end")})],
            [[s.Node("start"), s.Node("end")]],
        ),
        (
            [
                s.Edge({s.Node("start"), s.Node("a")}),
                s.Edge({s.Node("a"), s.Node("end")}),
                s.Edge({s.Node("start"), s.Node("b")}),
                s.Edge({s.Node("b"), s.Node("end")}),
            ],
            [
                [s.Node("start"), s.Node("a"), s.Node("end")],
                [s.Node("start"), s.Node("b"), s.Node("end")],
            ],
        ),
        (
            [
                s.Edge({s.Node("start"), s.Node("A")}),
                s.Edge({s.Node("A"), s.Node("end")}),
                s.Edge({s.Node("A"), s.Node("b")}),
            ],
            [
                [
                    s.Node("start"),
                    s.Node("A"),
                    s.Node("end"),
                ],
                [
                    s.Node("start"),
                    s.Node("A"),
                    s.Node("b"),
                    s.Node("A"),
                    s.Node("end"),
                ],
            ],
        ),
    ),
)
def test_get_paths_from_node(edges, paths):
    assert s.get_paths_from_node(s.Node("start"), edges) == paths
