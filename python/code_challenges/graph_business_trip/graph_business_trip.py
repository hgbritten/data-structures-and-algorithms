def business_trip(graph, cities):
    total = 0
    counter = 1
    tripdone = len(cities) - 1
    city_nodes = graph.get_nodes()
    origin = None

    for city in city_nodes:
        if city.value == cities[0]:
            origin = city

    while tripdone > 0:
        edges = graph.get_neighbors(origin)
        for count, edge in enumerate(edges):
            print("LOOK HERE", edge.vertex.value, cities[counter])
            if edge.vertex.value == cities[counter]:
                counter += 1
                total += edge.weight
                tripdone -= 1
                origin = edge.vertex
                break
            elif len(edges) - 1 == count:
                return False, "0$"

    return True, str(total) + "$"
