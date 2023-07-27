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

	with open(os.path.join(datapath,'rosalind_ba1j.txt')) as f:
		# read data
		genome = f.readline().strip()
		k,d = [int(x) for x in f.readline().strip().split()]


def revc(dna):
	return ''.join([{'A':'T','T':'A','C':'G','G':'C'}[i] for i in dna])[::-1]

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

def find_frequent_words_with_mismatches_and_revcomp(genome,k,d):
	kmers = []
	for i in range(len(genome)-k+1):
		pattern = genome[i:i+k]
		kmers.extend(neighbors(pattern,d))
	revc_genome = revc(genome)
	for i in range(len(revc_genome)-k+1):
		pattern = revc_genome[i:i+k]
		kmers.extend(neighbors(pattern,d))
	
	freqs= {}
	for kmer in kmers:
		if kmer in freqs:
			freqs[kmer] += 1
		else:
			freqs[kmer] = 1
	
	max_freq = max(freqs.values())
	return [kmer for kmer in freqs if freqs[kmer] == max_freq]

print(' '.join(find_frequent_words_with_mismatches_and_revcomp(genome,k,d)))