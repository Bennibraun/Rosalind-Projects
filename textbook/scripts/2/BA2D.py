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

	path = os.path.join(datapath,'rosalind_ba2d.txt')
	if os.path.exists(path):
		with open(path) as f:
			k,t = [int(x) for x in f.readline().strip().split()]
			dna = [line.strip() for line in f.readlines()]
		


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

def make_profile(dna,k,n):
	mat_rows = ['A','C','G','T']
	profile = [[],[],[],[]]
	for i in range(n,k+n):
		kth_nucs = [dna[j][i] for j in range(len(dna))]
		counts = [kth_nucs.count(nuc) for nuc in mat_rows]
		probs = [count/sum(counts) for count in counts]
		for j in range(len(probs)):
			profile[j].append(probs[j])
	return profile

def get_motifs(dna,k,n):
	return [dna_i[n:n+k] for dna_i in dna]

def hamming_distance(p,q):
	hamming = 0
	for i in range(len(p)):
		if p[i] != q[i]:
			hamming += 1
	return hamming

def score(motifs):
	consensus = ''
	for i in range(len(motifs[0])):
		nucs = [motifs[j][i] for j in range(len(motifs))]
		consensus += max(set(nucs),key=nucs.count)
	score = 0
	for motif in motifs:
		score += hamming_distance(motif,consensus)
	return score

def greedy_motif_search(dna,k,t):
	best_motifs = get_motifs(dna,k,0)
	mat_rows = ['A','C','G','T']
	for motif in [dna[0][j:j+k] for j in range(len(dna[0])-k+1)]:
		print(motif)
		motif1 = motif
		motifs = [motif1]
		for i in range(1,t):
			motif_i = get_motifs(dna,k,i)
			print('motif_i:',motif_i)
			profile = make_profile(motif_i,k,0)
			motifs.append(profile_most_probable_kmer(dna[i],profile))
			print('motifs: ',motifs)
		if score(motifs) < score(best_motifs):
			best_motifs = motifs
			print('best motif: ',best_motifs)
	return best_motifs


# 3 5
# GGCGTTCAGGCA
# AAGAATCAGTCA
# CAAGGAGTTCGC
# CACGTCAATCAC
# CAATAATATTCG
print('\n'.join(greedy_motif_search(['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG'],3,5)))

# 3 4
# GCCCAA GGCCTG AACCTA TTCCTT
# print(greedy_motif_search(['GCCCAA','GGCCTG','AACCTA','TTCCTT'],3,4))

# print('\n'.join(greedy_motif_search(dna,k,t)))