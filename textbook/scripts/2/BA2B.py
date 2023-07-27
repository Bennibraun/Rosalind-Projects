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

	path = os.path.join(datapath,'rosalind_ba2b.txt')
	if os.path.exists(path):
		with open(path) as f:
			k = int(f.readline().strip())
			dna = [x.strip() for x in f.readlines()]


# Exercise: max possible value of Score(motifs) in terms of t and k (t x k matrix)
# Max score for one column is given by each nuc being equal, so that 0.75t fail to match
# This yields a score of k * floor(0.75t)
# floored because when t%4!=0, one nuc will need to be represented one more time than the others, so we have to round down on the final mismatch score

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

def hamming_distance(p,q):
	hamming = 0
	for i in range(len(p)):
		if p[i] != q[i]:
			hamming += 1
	return hamming

# d
def dist(pattern,dna):
	k = len(pattern)
	distance = 0
	for text in dna:
		hamming_dist = 100000
		for i in range(len(text)-k+1):
			pattern2 = text[i:i+k]
			hamming_dist = min(hamming_dist,hamming_distance(pattern,pattern2))
		distance += hamming_dist
	return distance

# Median string
def median_string(dna,k):
	distance = 100000
	median = ''
	for i in range(4**k):
		pattern = number_to_pattern(i,k)
		d = dist(pattern,dna)
		if d < distance:
			# print(pattern,d)
			distance = d
			median = pattern
	return median


# print(dist('GATTCTCA','GCAAAGACGCTGACCAA'))
# print(median_string(['AAATTGACGCAT','GACGACCACGTT','CGTCAGCGCCTG','GCTGAGCACCGG','AGTACGGGACAG'],3))
print(median_string(dna,k))