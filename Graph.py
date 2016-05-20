class Graph:
    def __init__(self):
        self.adj_dict = dict()
        self.vertices = []

    def get_vertices(self):
        return self.vertices

    def get_connections(self, src):
        if src not in self.adj_dict:
            return []
        else:
            return self.adj_dict[src]

    def add_directed_edge(self, src_v, dest_v):
        # add vertices to vertices array
        if src_v not in self.vertices:
            self.vertices.append(src_v)
        if dest_v not in self.vertices:
            self.vertices.append(dest_v)

        # add edge to adjacency dictionary
        if src_v in self.adj_dict:
            if dest_v not in self.adj_dict[src_v]:
                self.adj_dict[src_v].append(dest_v)
        else:
            self.adj_dict[src_v] = [dest_v]

    def add_undirected_edge(self, vert_1, vert_2):
        self.add_directed_edge(vert_1, vert_2)
        self.add_directed_edge(vert_2, vert_1)

    def add_mult_directed_edges(self, src, destinations):
        for dest in destinations:
            self.add_directed_edge(src, dest)

    def add_mult_undirected_edges(self, src, destinations):
        for dest in destinations:
            self.add_undirected_edge(src, dest)

    def __str__(self):
        vertices = sorted(self.vertices)
        s = "Graph Edges:"

        for v in vertices:
            connected = []

            if v in self.adj_dict:
                connected = sorted(self.adj_dict[v])

            s += "\n{} -> {}".format(v, connected)

        return s

if __name__ == '__main__':
    g = Graph()
    g.add_undirected_edge("A","B")
    g.add_directed_edge("A", "C")
    g.add_directed_edge("A", "B")
    g.add_directed_edge("D", "C")
    print(g)