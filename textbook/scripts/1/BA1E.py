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

	with open(os.path.join(datapath,'rosalind_ba1e.txt')) as f:
		# read data
		genome = f.readline().strip()
		k, L, t = [int(x) for x in f.readline().strip().split(' ')]


def symbol_to_number(symbol):
	return {'A':0,'C':1,'G':2,'T':3}[symbol]

def pattern_to_number(pattern):
	if len(pattern) == 0:
		return 0
	symbol = pattern[-1]
	prefix = pattern[:-1]
	return 4*pattern_to_number(prefix) + symbol_to_number(symbol)

def number_to_symbol(number):
	return {0:'A',1:'C',2:'G',3:'T'}[number]

def number_to_pattern(index,k):
	if k == 1:
		return number_to_symbol(index)
	prefix_index = index // 4
	r = index % 4
	symbol = number_to_symbol(r)
	prefix_pattern = number_to_pattern(prefix_index,k-1)
	return prefix_pattern + symbol


def find_frequent_words(genome,k):
	kmers = []
	for i in range(len(genome)-k+1):
		pattern_num = pattern_to_number(genome[i:i+k])
		kmers.append(pattern_num)
	kmers.sort()
	freqs= {}
	for kmer in kmers:
		if kmer in freqs:
			freqs[kmer] += 1
		else:
			freqs[kmer] = 1
	return freqs


def find_clumps(genome,k,L,t):
	freq_patterns = set()
	freqs = find_frequent_words(genome[:L],k)
	for i in range(len(genome)-L):
		text = genome[i:i+L]
		for kmer in freqs:
			if freqs[kmer] >= t:
				freq_patterns.add(number_to_pattern(kmer,k))
		
		# remove first kmer
		first_kmer = pattern_to_number(text[:k])
		freqs[first_kmer] -= 1
		# add last kmer
		last_kmer = pattern_to_number(text[-k:])
		if last_kmer in freqs:
			freqs[last_kmer] += 1
		else:
			freqs[last_kmer] = 1
	
	return freq_patterns

# genome = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
# k, L, t = [int(x) for x in '5 75 4'.split(' ')]

print(' '.join(find_clumps(genome,k,L,t)))