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

	path = os.path.join(datapath,'rosalind_ba3d.txt')
	if os.path.exists(path):
		with open(path) as f:
			k = int(f.readline().strip())
			text = f.readline().strip()



def debruijn_graph(text,k):
	# make a dictionary for edges in a directed graph, using the starting node as the key and the ending node as the value
	# edges = set([text[i:i+k-1] for i in range(len(text)-k+2)])
	edges = {node:[] for node in list(set([text[i:i+k-1] for i in range(len(text)-k+2)]))}
	# print(edges)
	
	# iterate through text, adding edges between nodes. A single node can connect to multiple nodes, which are delimited by commas
	for i in range(len(text)-k+1):
		edges[text[i:i+k-1]].append(text[i+1:i+k])
	
	# create print format of adjacency list
	adjacency_list = []
	for node in edges:
		if len(edges[node]) > 0:
			adjacency_list.append(node + ' -> ' + ','.join(edges[node]))
	return adjacency_list
	

# print('\n'.join(debruijn_graph('AAGATTCTCTAC',4)))
# print('\n'.join(debruijn_graph(text,k)))

# write to output file
with open(os.path.join(datapath,'rosalind_ba3d_output.txt'),'w') as outputfile:
	outputfile.write('\n'.join(debruijn_graph(text,k)))