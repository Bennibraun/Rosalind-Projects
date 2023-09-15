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

	path = os.path.join(datapath,'rosalind_ba3c.txt')
	if os.path.exists(path):
		with open(path) as f:
			patterns = [line.strip() for line in f.readlines()]


def overlap_graph(patterns):
	adjacency_list = []
	for pattern in patterns:
		for pattern2 in patterns:
			if pattern[1:] == pattern2[:-1]:
				adjacency_list.append(pattern + ' -> ' + pattern2)
	return adjacency_list

# print('\n'.join(overlap_graph(['ATGCG','GCATG','CATGC','AGGCA','GGCAT'])))
print('\n'.join(overlap_graph(patterns)))