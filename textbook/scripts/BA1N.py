if __name__ == '__main__':
	import os
	import glob

	datapath = []
	if 'textbook' in glob.glob('*'):
		datapath.append('textbook')
		datapath.append('data')
	elif len(glob.glob('*.py')) > 0:
		datapath.append('..')
		datapath.append('data')
	datapath = os.path.join(*datapath)

	with open(os.path.join(datapath,'rosalind_ba1n.txt')) as f:
		# read data
		pattern = f.readline().strip()
		d = int(f.readline().strip())

def hamming_distance(p,q):
	hamming = 0
	for i in range(len(p)):
		if p[i] != q[i]:
			hamming += 1
	return hamming

def immediate_neighbors(pattern):
	neighborhood = set()
	for i in range(len(pattern)):
		symbol = pattern[i]
		for x in 'ACGT':
			neighborhood.add(pattern[:i]+x+pattern[i+1:])
	return neighborhood

def neighbors(pattern,d):
	if d == 0:
		return {pattern}
	if len(pattern) == 1:
		return {'A','C','G','T'}
	neighborhood = set()
	suffix_neighbors = neighbors(pattern[1:],d)
	for text in suffix_neighbors:
		if hamming_distance(pattern[1:],text) < d:
			for x in 'ACGT':
				neighborhood.add(x+text)
		else:
			neighborhood.add(pattern[0]+text)
	return neighborhood


print(*neighbors(pattern,d),sep='\n')
