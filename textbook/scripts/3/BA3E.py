if __name__ == '__main__':
	import os
	import glob

	datapath = []
	if 'textbook' in glob.glob('*'):
		datapath.append('textbook')
		datapath.append('data')
	elif len(glob.glob('*.py')) > 0:
		datapath.extend(['..','..','data'])
	datapath = os.path.join(*datapath)

	path = os.path.join(datapath,'rosalind_ba3e.txt')
	if os.path.exists(path):
		with open(path) as f:
			patterns = f.readlines()
			patterns = [p.strip() for p in patterns]

def debruijn_from_kmers(patterns):
	# k = len(patterns[0])-1
	# edges = {node:[] for node in set(patterns)}
	# for i,p in enumerate(patterns):
	# 	for ii,pp in enumerate(patterns):
	# 		if ii==i:
	# 			continue
	# 		if p[1:] == pp[:k]:
	# 			edges[p].append(pp)

	# given a collection of k-mers, the nodes are simply all unique (k-1)-mers that are a prefix or suffix of any k-mer
	k = len(patterns[0])-1
	nodes = set()
	for p in patterns:
		nodes.add(p[1:])
		nodes.add(p[:k])
	
	# for every k-mer, we connect the prefix node and suffix node by a directed edge
	edges = {node:[] for node in nodes}
	for p in patterns:
		edges[p[:k]].append(p[1:])
	
	
	
	# create print format of adjacency list
	adjacency_list = []
	for node in edges:
		if len(edges[node]) > 0:
			adjacency_list.append(node + ' -> ' + ','.join(edges[node]))
	
	return adjacency_list

# print(debruijn_from_kmers(['GAGG','CAGG','GGGG','GGGA','CAGG','AGGG','GGAG']))

# write to output file
with open(os.path.join(datapath,'rosalind_ba3e_output.txt'),'w') as outputfile:
	outputfile.write('\n'.join(debruijn_from_kmers(patterns)))