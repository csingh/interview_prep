import sys
sys.path.insert(0, '../../')

from Graph import *

def build_order(projects, dependencies):

    def recurser(proj):
        if proj in visited: return
        visited.append(proj)
        if proj not in resolved:
            # resolve all dependencies first
            # print("not resolved")
            for dep in proj_dependencies[proj]:
                if dep not in resolved:
                    # print("recursing to resolve {}'s dependency on {}".format(proj, dep))
                    recurser(dep)
            resolved.append(proj)
            order.append(proj)

        # print("resolved:", resolved)
        # move to dependents
        for dependent in graph.get_connections(proj):
            # print("recursing to move to {}'s dependent {}".format(proj, dependent))
            recurser(dependent)

    order = []
    graph = Graph()
    resolved = []
    visited = []

    # init proj_dependencies
    proj_dependencies = dict()
    for p in projects:
        proj_dependencies[p] = []

    # make dependents graph
    for d in dependencies:
        proj = d[0]
        depends_on = d[1]
        proj_dependencies[proj].append(depends_on)
        graph.add_directed_edge(depends_on, proj)

    print("proj_dependencies:", proj_dependencies)
    print(graph)

    # find the projects with 0 dependencies
    zero_dependencies = []
    for proj,deps in proj_dependencies.items():
        print(proj, deps)
        if len(deps) == 0:
            zero_dependencies.append(proj)

    print("zero_dependencies:", zero_dependencies)

    # if everything is dependent on something, then
    # there is no way we can build
    if len(zero_dependencies) == 0: return None

    # we'll start with the projects with 0 dependencies
    order = zero_dependencies[:]
    resolved = zero_dependencies[:]

    for proj in zero_dependencies:
        recurser(proj)

    return order

if __name__ == '__main__':
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [
        ("d", "a"),
        ("b", "f"),
        ("d", "b"),
        ("a", "f"),
        ("c", "d")
        ]
    print(build_order(projects, dependencies))