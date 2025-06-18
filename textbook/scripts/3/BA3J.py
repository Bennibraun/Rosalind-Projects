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

    path = os.path.join(datapath, "rosalind_ba3j.txt")
    if os.path.exists(path):
        with open(path) as f:
            lines = [line.strip() for line in f.readlines()]
            k, d = map(int, lines[0].split())
            paired_reads = [tuple(line.split("|")) for line in lines[1:]]

from collections import defaultdict


def build_paired_de_bruijn_graph(paired_reads):
    graph = defaultdict(list)
    for (p1, p2) in paired_reads:
        prefix = (p1[:-1], p2[:-1])
        suffix = (p1[1:], p2[1:])
        graph[prefix].append(suffix)
    return graph


def find_start_node(graph):
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    nodes = set()

    for u in graph:
        outdegree[u] += len(graph[u])
        nodes.add(u)
        for v in graph[u]:
            indegree[v] += 1
            nodes.add(v)

    for node in nodes:
        if outdegree[node] - indegree[node] == 1:
            return node  # unique start node
    for node in graph:
        if graph[node]:
            return node
    return None


def hierholzer(graph):
    graph = {k: list(v) for k, v in graph.items()}
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


def reconstruct_string_from_path(path, k, d):
    prefix_string = path[0][0]
    suffix_string = path[0][1]
    for p, s in path[1:]:
        prefix_string += p[-1]
        suffix_string += s[-1]
    # Now combine prefix and suffix with gap d
    return prefix_string + suffix_string[-(k + d):]


def string_reconstruction_from_paired_reads(paired_reads, k, d):
    graph = build_paired_de_bruijn_graph(paired_reads)
    path = hierholzer(graph)
    return reconstruct_string_from_path(path, k, d)


if __name__ == "__main__":
    result = string_reconstruction_from_paired_reads(paired_reads, k, d)
    print(result)
