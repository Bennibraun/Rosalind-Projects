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

	path = os.path.join(datapath,'rosalind_ba2c.txt')
	if os.path.exists(path):
		with open(path) as f:
			dna = f.readline().strip()
			k = int(f.readline().strip())
			profile = []
			for line in f:
				profile.append([float(i) for i in line.strip().split()])


def probability(kmer,profile):
	#profile is a 4xk matrix
	mat_rows = ['A','C','G','T']
	k_row = [mat_rows.index(kmer[0])]
	prob_n = profile[k_row[0]][0]
	if prob_n == 0:
		return 0
	elif len(kmer) == 1:
		return prob_n
	else:
		return prob_n * probability(kmer[1:],[profile[i][1:] for i in range(4)])


def profile_most_probable_kmer(dna,profile):
	#profile is a 4xk matrix
	k = len(profile[0])
	max_prob = 0
	for kmer in [dna[i:i+k] for i in range(len(dna)-k+1)]:
		prob = probability(kmer,profile)
		if prob > max_prob:
			max_prob = prob
			max_kmer = kmer
	return max_kmer

# print(profile_most_probable_kmer('ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT',[[0.2,0.2,0.3,0.2,0.3],[0.4,0.3,0.1,0.5,0.1],[0.3,0.3,0.5,0.2,0.4],[0.1,0.2,0.1,0.1,0.2]]))
print(profile_most_probable_kmer(dna,profile))