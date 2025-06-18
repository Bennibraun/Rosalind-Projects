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

	path = os.path.join(datapath, "rosalind_ba3k.txt")
	if os.path.exists(path):
		with open(path) as f:
			kmers = [line.strip() for line in f.readlines()]

from collections import defaultdict


def build_de_bruijn_graph(kmers):
	graph = defaultdict(list)
	for kmer in kmers:
		prefix = kmer[:-1]
		suffix = kmer[1:]
		graph[prefix].append(suffix)
	return graph


def calculate_indegree_outdegree(graph):
	indegree = defaultdict(int)
	outdegree = defaultdict(int)

	for u in graph:
		outdegree[u] += len(graph[u])
		for v in graph[u]:
			indegree[v] += 1

	nodes = set(list(indegree.keys()) + list(outdegree.keys()))
	for node in nodes:
		if node not in indegree:
			indegree[node] = 0
		if node not in outdegree:
			outdegree[node] = 0
	return indegree, outdegree

def maximal_non_branching_paths(graph):
    indegree, outdegree = calculate_indegree_outdegree(graph)
    paths = []

    # Track number of times each edge appears
    edge_counts = defaultdict(lambda: defaultdict(int))
    for u in graph:
        for v in graph[u]:
            edge_counts[u][v] += 1

    def has_unused_edge(u):
        return any(count > 0 for count in edge_counts[u].values())

    for node in graph:
        # non-branching path start nodes
        if outdegree[node] != 1 or indegree[node] != 1:
            for nbr in graph[node]:
                while edge_counts[node][nbr] > 0:
                    path = [node, nbr]
                    edge_counts[node][nbr] -= 1
                    current = nbr
                    while indegree[current] == 1 and outdegree[current] == 1:
                        next_node = graph[current][0]  # must be only one
                        if edge_counts[current][next_node] == 0:
                            break
                        path.append(next_node)
                        edge_counts[current][next_node] -= 1
                        current = next_node
                    paths.append(path)

    # isolated cycles (1-in-1-out nodes only)
    for node in graph:
        while outdegree[node] == 1 and indegree[node] == 1:
            next_node = graph[node][0]
            if edge_counts[node][next_node] == 0:
                break
            # start a cycle
            cycle = [node, next_node]
            edge_counts[node][next_node] -= 1
            current = next_node
            while current != node:
                next_node = graph[current][0]
                cycle.append(next_node)
                edge_counts[current][next_node] -= 1
                current = next_node
            paths.append(cycle)

    return paths



def path_to_string(path):
	s = path[0]
	for node in path[1:]:
		s += node[-1]
	return s


def contigs_from_kmers(kmers):
	graph = build_de_bruijn_graph(kmers)
	paths = maximal_non_branching_paths(graph)
	return [path_to_string(p) for p in paths]


if __name__ == "__main__":
	contigs = contigs_from_kmers(kmers)
	print(" ".join(contigs))