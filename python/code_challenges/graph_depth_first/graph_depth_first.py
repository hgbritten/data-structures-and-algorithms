class Graph:
    def __init__(self, kind="single direction"):
        self._adjacency_list = {}
        self.type = kind

    def add_node(self, value):
        v = Vertex(value)
        if v not in self._adjacency_list:
            self._adjacency_list[v] = {}
            return v

    def size(self):
        return len(self._adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not found in graph")

        self._adjacency_list[start_vertex][end_vertex] = weight

        if self.type == "bidirectional":
            self._adjacency_list[end_vertex][start_vertex] = weight

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex)


class Vertex:
    def __init__(self, value):
        self.value = value


def depth_first_pre_order(graph):
    visited = {}
    collection = []
    first_vertex = list(graph._adjacency_list.keys())[0]

    def walk(start_vertex):
        nonlocal visited, collection, graph
        if start_vertex is None:
            return
        if start_vertex not in visited:
            collection.append(start_vertex)
            visited[start_vertex] = True
        if graph._adjacency_list.get(start_vertex):
            for end_vertex in graph._adjacency_list.get(start_vertex):
                walk(end_vertex)

    walk(first_vertex)
    return collection
