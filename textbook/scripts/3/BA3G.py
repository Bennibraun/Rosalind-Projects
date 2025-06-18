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

    path = os.path.join(datapath, "rosalind_ba3g.txt")
    if os.path.exists(path):
        with open(path) as f:
            adjacency_list = [line.strip() for line in f.readlines()]

from collections import defaultdict


def read_graph(adjacency_list):
    graph = defaultdict(list)
    for g in adjacency_list:
        node_a, _, nodes_b = g.split(" ")
        graph[node_a].extend(nodes_b.split(","))
    return graph


def find_start_node(graph):
    indegree = defaultdict(int)
    outdegree = defaultdict(int)

    for u in graph:
        outdegree[u] += len(graph[u])
        for v in graph[u]:
            indegree[v] += 1

    nodes = set(list(indegree.keys()) + list(outdegree.keys()))
    start = None
    for node in nodes:
        if outdegree[node] - indegree[node] == 1:
            return node  # valid start
    # fallback: try any node with outgoing edge
    for node in graph:
        if graph[node]:
            return node
    return None


def hierholzer(graph):
    graph = {k: list(v) for k, v in graph.items()}  # copy
    stack = []
    path = []
    curr = find_start_node(graph)
    stack.append(curr)

    while stack:
        if graph.get(curr) and graph[curr]:
            stack.append(curr)
            next_node = graph[curr].pop()
            curr = next_node
        else:
            path.append(curr)
            curr = stack.pop()
    path.reverse()
    return path


def eulerian_path(adjacency_list):
    graph = read_graph(adjacency_list)
    print(graph)
    path = hierholzer(graph)
    print("->".join(path))


eulerian_path(adjacency_list)
