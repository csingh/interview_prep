import sys
sys.path.insert(0, '../')

from Graph import *

def dfs(graph, src, dest):
    verts = graph.get_vertices()
    if src not in verts or dest not in verts:
        return False

    visited = dict()
    for vert in verts:
        visited[vert] = False

    def dfs_util(src, dest):
        if src == dest: return True

        visited[src] = True
        found = False
        for connected in graph.get_connections(src):
            if not visited[connected]:
                found = found or dfs_util(connected, dest)

        return found

    return dfs_util(src, dest)

def bfs(graph, src, dest):
    verts = graph.get_vertices()
    if src not in verts or dest not in verts:
        return False

    visited = dict()
    for vert in verts:
        visited[vert] = False

    queue = [src]

    while queue:
        vert = queue.pop(0)
        visited[vert] = True
        if vert == dest: return True
        for connected in graph.get_connections(vert):
            if not visited[connected] and connected not in queue:
                queue.append(connected)

    return False 

if __name__ == '__main__':
    # A - B - C
    # | \ | / |
    # D - E - F
    g = Graph()
    g.add_mult_undirected_edges("A", ["B", "D", "E"])
    g.add_mult_undirected_edges("B", ["A", "C", "E"])
    g.add_mult_undirected_edges("C", ["B", "E", "F"])
    g.add_mult_undirected_edges("D", ["A", "E"])
    g.add_mult_undirected_edges("E", ["A", "B", "C", "D", "F"])
    g.add_mult_undirected_edges("F", ["C", "E"])

    print(g)
    print("----------------------")

    # dfs assertion tests
    assert dfs(g, "A", "B") == True
    assert dfs(g, "A", "not exists") == False
    assert dfs(g, "A", "F") == True

    # bfs assertion tests
    assert bfs(g, "A", "B") == True
    assert bfs(g, "A", "not exists") == False
    assert bfs(g, "A", "F") == True

    print("Assertion tests passed.")
