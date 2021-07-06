import pytest
from code_challenges.graph.graph import Graph, Vertex


# @pytest.mark.skip("pending")
def test_add_node():
    graph = Graph()
    expected = "spam"
    actual = graph.add_node("spam")
    assert actual.value == expected


def test_add_node2():
    graph = Graph()
    graph.add_node("spam")
    actual = graph.get_nodes()
    expected = 1
    assert len(actual) == expected
    assert isinstance(actual[0], Vertex)
    assert actual[0].value == "spam"


def test_get_nodes():
    g = Graph()
    g.add_node("spam")
    g.add_node("eggs")

    actual = g.get_nodes()

    expected = 2

    assert len(actual) == expected

    assert isinstance(actual[0], Vertex)
    assert isinstance(actual[1], Vertex)

    assert actual[0].value == "spam"
    assert actual[1].value == "eggs"


def test_size_two():
    g = Graph()
    g.add_node("spam")
    g.add_node("eggs")
    actual = g.size()
    expected = 2
    assert actual == expected


def test_add_edge_no_weight():
    g = Graph()
    sv = g.add_node("spam")
    ev = g.add_node("eggs")
    ret_val = g.add_edge(sv, ev)

    assert ret_val is None


def test_get_neighbors():
    g = Graph()
    sv = g.add_node("spam")
    ev = g.add_node("eggs")
    g.add_edge(sv, ev, 5)
    neighbors = g.get_neighbors(sv)

    assert len(neighbors) == 1
    se = neighbors[0]

    assert se.vertex.value == "eggs"
    assert se.weight == 5


def test_get_n_solo():
    g = Graph()
    sv = g.add_node("spam")
    g.add_edge(sv, sv)

    neighbors = g.get_neighbors(sv)

    assert len(neighbors) == 1
    se = neighbors[0]

    assert se.vertex.value == "spam"
    assert se.weight == 0


def test_get_neighbors_45():
    g = Graph()
    pv = g.add_node("Pandora")
    av = g.add_node("Arendelle")
    mv = g.add_node("Metroville")
    mov = g.add_node("Monstropolis")
    nv = g.add_node("Naboo")
    narv = g.add_node("Narnia")

    g.add_edge(pv, av, 150)
    g.add_edge(pv, mv, 82)
    g.add_edge(av, mov, 42)
    g.add_edge(av, mv, 99)
    g.add_edge(mv, mov, 105)
    g.add_edge(mv, narv, 37)
    g.add_edge(mv, nv, 26)
    g.add_edge(nv, mov, 73)
    g.add_edge(nv, narv, 250)

    neighbors = g.get_neighbors(pv)

    assert len(neighbors) == 2
    se = neighbors[0]
    me = neighbors[1]

    assert se.vertex.value == "Arendelle"
    assert me.vertex.value == "Metroville"

    assert se.weight == 150
    assert me.weight == 82


def test_get_neighbors_43():
    g = Graph()
    pv = g.add_node("Pandora")
    av = g.add_node("Arendelle")
    mv = g.add_node("Metroville")
    mov = g.add_node("Monstropolis")
    nv = g.add_node("Naboo")
    narv = g.add_node("Narnia")

    g.add_edge(pv, av, 150)
    g.add_edge(pv, mv, 82)
    g.add_edge(av, mov, 42)
    g.add_edge(av, mv, 99)
    g.add_edge(mv, mov, 105)
    g.add_edge(mv, narv, 37)
    g.add_edge(mv, nv, 26)
    g.add_edge(nv, mov, 73)
    g.add_edge(nv, narv, 250)

    neighbors = g.get_neighbors(mv)

    assert len(neighbors) == 3
    se = neighbors[0]
    me = neighbors[1]
    te = neighbors[2]

    assert se.vertex.value == "Monstropolis"
    assert me.vertex.value == "Narnia"
    assert te.vertex.value == "Naboo"

    assert se.weight == 105
    assert me.weight == 37
