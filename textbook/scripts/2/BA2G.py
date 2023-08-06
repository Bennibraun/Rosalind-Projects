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

	path = os.path.join(datapath,'rosalind_ba2g.txt')
	if os.path.exists(path):
		with open(path) as f:
			k,t,N = [int(x) for x in f.readline().strip().split()]
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

def make_profile_laplace_gibbs(dna,k,start,i):
    mat_rows = ['A','C','G','T']
    profile = [[],[],[],[]]
    for i in range(start,start+k):
        kth_nucs = [dna[j][i] for j in range(len(dna)) if len(dna[j]) > i and j != i]
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

def profile_random_kmer(dna,profile,k):
	# profile is a 4xk matrix
	probs = []
	for i in range(len(dna)-k+1):
		kmer = dna[i:i+k]
		probs.append(probability(kmer,profile))
	random_i = random_gibbs(probs)
	return dna[random_i:random_i+k]

def random_gibbs(p):
	c = sum(p)
	p = [x/c for x in p]
	# print(p)
	r = random.random()
	# print(r)
	# return the index of the integer in p which is closest to r without going over
	for i in range(len(p)):
		# print(p[i])
		if r < p[i]:
			return i
		r -= p[i]

def gibbs_sampler(dna, k, t, n):
	motifs = []
	for i in range(t):
		start = random.randint(0,len(dna[i])-k)
		motifs.append(dna[i][start:start+k])
	best_motifs = motifs
	for j in range(n):
		i = int(random.random()*t)
		profile = make_profile_laplace_gibbs(motifs,k,0,i)
		motifs[i] = profile_random_kmer(dna[i],profile,k)
		if score(motifs) < score(best_motifs):
			best_motifs = motifs
	return best_motifs, score(best_motifs)

best_m = []
best_s = 100000
for s in range(20):
	# m,s = gibbs_sampler(['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA'],8,5,100)
	m,s = gibbs_sampler(dna,k,t,N)
	# print(m)
	if s < best_s:
		best_m = m
		best_s = s

print('\n'.join(best_m))
