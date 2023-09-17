if __name__ == "__main__":
    import os
    import glob

    datapath = []
    if "textbook" in glob.glob("*"):
        datapath.append("textbook")
        datapath.append("data")
    elif len(glob.glob("*.py")) > 0:
        datapath.extend(["..", "..", "data"])
    datapath = os.path.join(*datapath)

    path = os.path.join(datapath, "rosalind_ba3f.txt")
    if os.path.exists(path):
        with open(path) as f:
            adjacency_list = [line.strip() for line in f.readlines()]

import random


def read_graph(adjacency_list):
    graph = {}
    for g in adjacency_list:
        node_a, _, nodes_b = g.split(" ")
        graph[node_a] = nodes_b.split(",")
    return graph


def random_walk(graph, start_node):
    curr = start_node
    next = random.choice(graph[curr])
    cycle = [(curr, next)]
    remaining_graph = remove_edge(graph, (curr, next))
    while start_node != next:
        curr = next
        next = random.choice(remaining_graph[curr])
        remaining_graph = remove_edge(remaining_graph, (curr, next))
        cycle.append((curr, next))
    return remaining_graph, cycle


def remove_edge(graph, edge):
    if len(graph[edge[0]]) <= 1:
        del graph[edge[0]]
    else:
        edges = graph[edge[0]]
        edges.remove(edge[1])
        graph[edge[0]] = edges
    return graph


def eulerian_cycle(adjacency_list):
    #  form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
    # while there are unexplored edges in Graph
    # 	select a node newStart in Cycle with still unexplored edges
    # 	form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
    # 	Cycle ← Cycle’
    # return Cycle
    graph = read_graph(adjacency_list)
    all_edges = set()
    for node_a, node_b in graph.items():
        [all_edges.add((node_a, b)) for b in node_b]
    remaining_graph, cycle = random_walk(graph, random.choice(list(graph.keys())))
    remaining_graph = graph.copy()
    while set(cycle) != all_edges:
        visited_nodes = [e[0] for e in cycle]
        for node in list(remaining_graph.keys()):
            if node in visited_nodes:
                new_start = node
                break
        remaining_graph, new_cycle = random_walk(remaining_graph, new_start)
        for i, edge in enumerate(cycle):
            if edge[0] == new_start:
                cycle = cycle[:i] + new_cycle + cycle[i:]
                break

    print(cycle[0][0], end="")
    for edge in cycle:
        print("->" + edge[1], end="")


# eulerian_cycle(
#     """0 -> 3
# 1 -> 0
# 2 -> 1,6
# 3 -> 2
# 4 -> 2
# 5 -> 4
# 6 -> 5,8
# 7 -> 9
# 8 -> 7
# 9 -> 6""".split(
#         "\n"
#     )
# )

eulerian_cycle(adjacency_list)
