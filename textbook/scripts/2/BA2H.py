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

	path = os.path.join(datapath,'rosalind_ba2h.txt')
	if os.path.exists(path):
		with open(path) as f:
			pattern = f.readline().strip()
			dna = f.readline().strip().split()



def hamming_distance(p,q):
	hamming = 0
	for i in range(len(p)):
		if p[i] != q[i]:
			hamming += 1
	return hamming

def distance_btw_pattern_and_strings(pattern,dna):
	k = len(pattern)
	distance = 0
	for text in dna:
		hamming = 1000000000
		for p in [text[i:i+k] for i in range(len(text)-k+1)]:
			if hamming > hamming_distance(pattern,p):
				hamming = hamming_distance(pattern,p)
		distance += hamming
	return distance

# print(distance_btw_pattern_and_strings('AAA',['TTACCTTAAC','GATATCTGTC','ACGGCGTTCG','CCCTAAAGAG','CGTCAGAGGT']))
print(distance_btw_pattern_and_strings(pattern,dna))