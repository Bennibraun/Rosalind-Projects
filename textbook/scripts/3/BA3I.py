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

    path = os.path.join(datapath, "rosalind_ba3i.txt")
    if os.path.exists(path):
        with open(path) as f:
            # first line is k
            lines = [line.strip() for line in f.readlines()]
            k = int(lines[0])

from collections import defaultdict


def build_de_bruijn_graph_binary(k):
    """Build De Bruijn graph of (k-1)-mers with binary alphabet for order k."""
    from itertools import product

    nodes = [''.join(p) for p in product('01', repeat=k-1)]
    graph = defaultdict(list)
    for node in nodes:
        # edges are node + '0' and node + '1' suffixes
        graph[node].append(node[1:] + '0')
        graph[node].append(node[1:] + '1')
    return graph


def hierholzer_cycle(graph):
    graph = {k: list(v) for k, v in graph.items()}
    stack = []
    cycle = []
    curr = next(iter(graph))  # arbitrary start node
    stack.append(curr)

    while stack:
        if graph.get(curr) and graph[curr]:
            stack.append(curr)
            next_node = graph[curr].pop()
            curr = next_node
        else:
            cycle.append(curr)
            curr = stack.pop()
    cycle.reverse()
    return cycle


def cycle_to_string(cycle):
    # cycle is list of (k-1)-mers forming a cycle, length = number of edges + 1 = 2^{k-1} + 1
    s = cycle[0]
    for node in cycle[1:-(k-1)]:
        s += node[-1]
    return s


def k_universal_circular_string(k):
    graph = build_de_bruijn_graph_binary(k)
    cycle = hierholzer_cycle(graph)
    return cycle_to_string(cycle)


if __name__ == "__main__":
    universal_string = k_universal_circular_string(k)
    print(universal_string)
