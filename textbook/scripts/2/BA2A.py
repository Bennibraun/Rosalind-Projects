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

	try:
		with open(os.path.join(datapath,'rosalind_ba2a.txt')) as f:
			k,d = [int(x) for x in f.readline().strip().split()]
			dna = [x.strip() for x in f.readlines()]
	except:
		pass

def hamming_distance(p,q):
	hamming = 0
	for i in range(len(p)):
		if p[i] != q[i]:
			hamming += 1
	return hamming

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


def motif_enumeration(dna, k, d):
	patterns = set()
	for dna_str in dna:
		for i in range(len(dna_str)-k):
			pattern = dna_str[i:i+k]
			neighborhood = neighbors(pattern,d)
			for p1 in neighborhood:
				p1_neighbors = neighbors(p1,d)
				for dna_str2 in dna:
					# if none of the neighbors are in dna_str2, break
					if not any([p2 in dna_str2 for p2 in p1_neighbors]):
						break
				else:
					patterns.add(p1)
	return patterns
						

# print(motif_enumeration(['ATTTGGC','TGCCTTA','CGGTATC','GAAAATT'],3,1))
print(' '.join(list(motif_enumeration(dna,k,d))))