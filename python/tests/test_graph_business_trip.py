from code_challenges.graph.graph import Graph, Edge, Vertex
from code_challenges.graph_business_trip.graph_business_trip import business_trip
import pytest


# @pytest.mark.skip("pending")
def test_get_neighbors_47():
    g = Graph()
    pv = g.add_node("Pandora")
    av = g.add_node("Arendelle")
    mv = g.add_node("Metroville")
    mov = g.add_node("Monstropolis")
    nv = g.add_node("Naboo")
    narv = g.add_node("Narnia")

    g.add_edge(pv, av, 150)
    g.add_edge(pv, mv, 82)
    g.add_edge(av, pv, 150)
    g.add_edge(av, mov, 42)
    g.add_edge(av, mv, 99)
    g.add_edge(mv, av, 99)
    g.add_edge(mv, pv, 82)
    g.add_edge(mv, mov, 105)
    g.add_edge(mv, narv, 37)
    g.add_edge(mv, nv, 26)
    g.add_edge(mov, av, 42)
    g.add_edge(mov, mv, 105)
    g.add_edge(mov, nv, 73)
    g.add_edge(nv, mov, 73)
    g.add_edge(nv, narv, 250)
    g.add_edge(nv, mv, 26)
    g.add_edge(narv, mv, 37)
    g.add_edge(narv, nv, 250)

    actual = business_trip(g, ["Pandora", "Arendelle", "Monstropolis"])
    expected = True, "192$"
    assert actual == expected


def test_get_neighbors_48():
    g = Graph()
    pv = g.add_node("Pandora")
    av = g.add_node("Arendelle")
    mv = g.add_node("Metroville")
    mov = g.add_node("Monstropolis")
    nv = g.add_node("Naboo")
    narv = g.add_node("Narnia")

    g.add_edge(pv, av, 150)
    g.add_edge(pv, mv, 82)
    g.add_edge(av, pv, 150)
    g.add_edge(av, mov, 42)
    g.add_edge(av, mv, 99)
    g.add_edge(mv, av, 99)
    g.add_edge(mv, pv, 82)
    g.add_edge(mv, mov, 105)
    g.add_edge(mv, narv, 37)
    g.add_edge(mv, nv, 26)
    g.add_edge(mov, av, 42)
    g.add_edge(mov, mv, 105)
    g.add_edge(mov, nv, 73)
    g.add_edge(nv, mov, 73)
    g.add_edge(nv, narv, 250)
    g.add_edge(nv, mv, 26)
    g.add_edge(narv, mv, 37)
    g.add_edge(narv, nv, 250)

    actual = business_trip(g, ["Metroville", "Arendelle", "Monstropolis", "Naboo"])
    expected = True, "214$"
    assert actual == expected


def test_get_neighbors_49():
    g = Graph()
    pv = g.add_node("Pandora")
    av = g.add_node("Arendelle")
    mv = g.add_node("Metroville")
    mov = g.add_node("Monstropolis")
    nv = g.add_node("Naboo")
    narv = g.add_node("Narnia")

    g.add_edge(pv, av, 150)
    g.add_edge(pv, mv, 82)
    g.add_edge(av, pv, 150)
    g.add_edge(av, mov, 42)
    g.add_edge(av, mv, 99)
    g.add_edge(mv, av, 99)
    g.add_edge(mv, pv, 82)
    g.add_edge(mv, mov, 105)
    g.add_edge(mv, narv, 37)
    g.add_edge(mv, nv, 26)
    g.add_edge(mov, av, 42)
    g.add_edge(mov, mv, 105)
    g.add_edge(mov, nv, 73)
    g.add_edge(nv, mov, 73)
    g.add_edge(nv, narv, 250)
    g.add_edge(nv, mv, 26)
    g.add_edge(narv, mv, 37)
    g.add_edge(narv, nv, 250)

    actual = business_trip(g, ["Metroville", "Pandora", "Monstropolis", "Naboo"])
    expected = False, "0$"
    assert actual == expected
