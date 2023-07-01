
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

	with open(os.path.join(datapath,'rosalind_ba1h.txt')) as f:
		# read data
		pattern = f.readline().strip()
		genome = f.readline().strip()
		d = int(f.readline().strip())

# pattern = 'ATTCTGGA'
# genome = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC'
# d = 3


def hamming_distance(p,q):
	hamming = 0
	for i in range(len(p)):
		if p[i] != q[i]:
			hamming += 1
	return hamming

def approximate_pattern_matching(pattern,genome,d):
	positions = []
	for i in range(len(genome)-len(pattern)+1):
		if hamming_distance(genome[i:i+len(pattern)],pattern) <= d:
			positions.append(i)
	return positions

print(' '.join([str(x) for x in approximate_pattern_matching(pattern,genome,d)]))