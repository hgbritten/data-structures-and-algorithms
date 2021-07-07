import pytest
from code_challenges.graph_depth_first.graph_depth_first import (
    Graph,
    depth_first_pre_order,
)


def test_depth_first():
    assert Graph


def test_Graph():
    assert depth_first_pre_order


def test_working():
    graph = Graph()
    nodes = {
        node: graph.add_node(node) for node in ["a", "b", "c", "d", "e", "f", "g", "h"]
    }

    graph.add_edge(nodes["a"], nodes["b"])
    graph.add_edge(nodes["a"], nodes["d"])
    graph.add_edge(nodes["b"], nodes["c"])
    graph.add_edge(nodes["b"], nodes["d"])
    graph.add_edge(nodes["c"], nodes["g"])
    graph.add_edge(nodes["d"], nodes["e"])
    graph.add_edge(nodes["d"], nodes["h"])
    graph.add_edge(nodes["a"], nodes["f"])
    result = depth_first_pre_order(graph)
    names_of_vertexs = [node.value for node in result]
    assert names_of_vertexs == ["a", "b", "c", "g", "d", "e", "h", "f"]


def test_fail_depth():

    graph = Graph()
    nodes = {
        node: graph.add_node(node) for node in ["a", "b", "c", "d", "e", "f", "g", "h"]
    }

    graph.add_edge(nodes["a"], nodes["b"])
    graph.add_edge(nodes["a"], nodes["d"])
    graph.add_edge(nodes["b"], nodes["c"])
    graph.add_edge(nodes["b"], nodes["d"])
    graph.add_edge(nodes["c"], nodes["g"])
    graph.add_edge(nodes["d"], nodes["e"])
    graph.add_edge(nodes["d"], nodes["h"])
    graph.add_edge(nodes["a"], nodes["f"])
    result = depth_first_pre_order(graph)
    names_of_vertexs = [node.value for node in result]
    assert names_of_vertexs != ["h", "b", "c", "g", "d", "e", "f", "a"]
