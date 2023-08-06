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

	path = os.path.join(datapath,'rosalind_ba2f.txt')
	if os.path.exists(path):
		with open(path) as f:
			k,t = [int(x) for x in f.readline().strip().split()]
			dna = [line.strip() for line in f.readlines()]

import random

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

def make_profile_laplace(dna,k,start):
    mat_rows = ['A','C','G','T']
    profile = [[],[],[],[]]
    for i in range(start,start+k):
        kth_nucs = [dna[j][i] for j in range(len(dna)) if len(dna[j]) > i]
        counts = [kth_nucs.count(nuc)+1 for nuc in mat_rows]
        sum_counts = sum(counts)
        probs = [count/sum_counts if sum_counts != 0 else 0 for count in counts]
        for j in range(len(probs)):
            profile[j].append(probs[j])
    return profile

def probability(kmer,profile):
    #profile is a 4xk matrix
    mat_rows = ['A','C','G','T']
    prob_n = 1
    for i in range(len(kmer)):
        prob_n *= profile[mat_rows.index(kmer[i])][i]
    return prob_n

def profile_most_probable_kmer(dna,profile,k):
    #profile is a 4xk matrix
    max_prob = 0
    max_kmer = ''
    for i in range(len(dna)-k+1):
        kmer = dna[i:i+k]
        prob = probability(kmer,profile)
        if prob > max_prob or max_kmer == '':
            max_prob = prob
            max_kmer = kmer
    return max_kmer

# RANDOMIZEDMOTIFSEARCH(Dna, k, t)
# 	randomly select k-mers Motifs = (Motif1, …, Motift) in each string
# 		from Dna
# 	BestMotifs ← Motifs
# 	while forever
# 		Profile ← Profile(Motifs)
# 		Motifs ← Motifs(Profile, Dna)
# 		if Score(Motifs) < Score(BestMotifs)
# 			BestMotifs ← Motifs
# 		else
# 			return BestMotifs


def randomized_motif_search(dna,k,t):
	motifs = []
	for i in range(t):
		start = random.randint(0,len(dna[i])-k)
		motifs.append(dna[i][start:start+k])
	best_motifs = motifs
	while True:
		profile = make_profile_laplace(motifs,k,0)
		motifs = [profile_most_probable_kmer(dna[i],profile,k) for i in range(t)]
		if score(motifs) < score(best_motifs):
			best_motifs = motifs
		else:
			return best_motifs, score(best_motifs)

best_score = 100000000
best_motifs = []
for i in range(1000):
	# motif_results, score_result = randomized_motif_search(['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
	# 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
	# 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA'],8,5)

	motif_results, score_result = randomized_motif_search(dna,k,t)

	if score_result < best_score:
		best_score = score_result
		best_motifs = motif_results

# print(best_score)
for motif in best_motifs:
	print(motif)