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

    path = os.path.join(datapath, "rosalind_ba3m.txt")
    if os.path.exists(path):
        with open(path) as f:
            adjacency_list = [line.strip() for line in f.readlines()]


from collections import defaultdict


def parse_adjacency_list(lines):
    graph = defaultdict(list)
    for line in lines:
        src, targets = line.split(" -> ")
        graph[int(src)] = [int(x) for x in targets.split(",")]
    return graph


def calculate_in_out_degrees(graph):
    indegree = defaultdict(int)
    outdegree = defaultdict(int)

    for u in graph:
        outdegree[u] = len(graph[u])
        for v in graph[u]:
            indegree[v] += 1

    # ensure all nodes are accounted for
    all_nodes = set(graph.keys()) | set(v for neighbors in graph.values() for v in neighbors)
    for node in all_nodes:
        if node not in indegree:
            indegree[node] = 0
        if node not in outdegree:
            outdegree[node] = 0

    return indegree, outdegree


def is_1_in_1_out(node, indegree, outdegree):
    return indegree[node] == 1 and outdegree[node] == 1


def maximal_non_branching_paths(graph):
    indegree, outdegree = calculate_in_out_degrees(graph)
    paths = []
    visited_edges = defaultdict(list)

    for node in graph:
        if not is_1_in_1_out(node, indegree, outdegree):
            if outdegree[node] > 0:
                for neighbor in graph[node]:
                    if neighbor in visited_edges[node]:
                        continue
                    path = [node, neighbor]
                    visited_edges[node].append(neighbor)
                    current = neighbor
                    while is_1_in_1_out(current, indegree, outdegree):
                        next_node = graph[current][0]
                        path.append(next_node)
                        visited_edges[current].append(next_node)
                        current = next_node
                    paths.append(path)

    # detect isolated cycles of 1-in-1-out nodes
    for node in graph:
        if is_1_in_1_out(node, indegree, outdegree):
            for neighbor in graph[node]:
                if neighbor not in visited_edges[node]:
                    cycle = [node, neighbor]
                    visited_edges[node].append(neighbor)
                    current = neighbor
                    while current != node:
                        next_node = graph[current][0]
                        cycle.append(next_node)
                        visited_edges[current].append(next_node)
                        current = next_node
                    paths.append(cycle)

    return paths


if __name__ == "__main__":
    graph = parse_adjacency_list(adjacency_list)
    paths = maximal_non_branching_paths(graph)
    for path in paths:
        print(" -> ".join(str(n) for n in path))
