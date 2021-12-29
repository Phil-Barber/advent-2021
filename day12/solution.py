import dataclasses


@dataclasses.dataclass
class Node:
    name: str

    def __hash__(self):
        return hash(self.name)

    @property
    def is_large(self):
        return self.name == self.name.upper() and not self.is_start and not self.is_end

    @property
    def is_start(self):
        return self.name == "start"

    @property
    def is_end(self):
        return self.name == "end"


@dataclasses.dataclass
class Edge:
    nodes: set[Node]

    @classmethod
    def from_string(cls, string):
        nodes = string.split("-")
        return Edge({Node(node) for node in nodes})


START = Node("start")
END = Node("end")


def get_num_paths_from_edges(raw_edges):
    edges = [Edge.from_string(edge_str) for edge_str in raw_edges]

    paths = get_paths_from_node(START, edges)

    return len(paths)


def get_paths_from_node(start_node, edges, path=None):
    path = [] if path is None else list(path)
    path.append(start_node)

    if start_node == END:
        return [path]

    next_edges = [edge for edge in edges for node in edge.nodes if node == start_node]
    next_nodes = [
        node
        for edge in next_edges
        for node in edge.nodes
        if node != start_node and (node.is_large or node not in path)
    ]
    return [
        node_path
        for node in next_nodes
        for node_path in get_paths_from_node(node, edges, path)
    ]


#####


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    inputs = [line[:-1] for line in inputs if line[0]]
    print(inputs[0])
    print(inputs[-1])
    answer = get_num_paths_from_edges(inputs)
    print(f"Answer: {answer}")
