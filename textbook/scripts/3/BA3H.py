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

    path = os.path.join(datapath, "rosalind_ba3h.txt")
    if os.path.exists(path):
        with open(path) as f:
            # first line is k, rest are k-mers
            lines = [line.strip() for line in f.readlines()]
            k = int(lines[0])
            kmers = lines[1:]

from collections import defaultdict


def build_de_bruijn(kmers):
    graph = defaultdict(list)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
    return graph


def find_start_node(graph):
    indegree = defaultdict(int)
    outdegree = defaultdict(int)

    for u in graph:
        outdegree[u] += len(graph[u])
        for v in graph[u]:
            indegree[v] += 1

    nodes = set(indegree.keys()) | set(outdegree.keys())
    for node in nodes:
        if outdegree[node] - indegree[node] == 1:
            return node
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


def reconstruct_string(path):
    s = path[0]
    for node in path[1:]:
        s += node[-1]
    return s


def eulerian_path_string_reconstruction(kmers):
    graph = build_de_bruijn(kmers)
    path = hierholzer(graph)
    return reconstruct_string(path)


result = eulerian_path_string_reconstruction(kmers)
print(result)
