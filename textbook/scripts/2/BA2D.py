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

def make_profile(dna,k,start):
    mat_rows = ['A','C','G','T']
    profile = [[],[],[],[]]
    for i in range(start,start+k):
        kth_nucs = [dna[j][i] for j in range(len(dna)) if len(dna[j]) > i]
        counts = [kth_nucs.count(nuc) for nuc in mat_rows]
        sum_counts = sum(counts)
        probs = [count/sum_counts if sum_counts != 0 else 0 for count in counts]
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
    best_motifs = [dna_i[0:k] for dna_i in dna]
    for i in range(len(dna[0])-k+1):
        motif = dna[0][i:i+k]
        motifs = [motif]
        for j in range(1,t):
            profile = make_profile(motifs,k,0)
            motifs.append(profile_most_probable_kmer(dna[j],profile,k))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


# print(score(get_motifs(['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG'],3,0)))
# print(make_profile(['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG'],3,0))

# 3 5
# GGCGTTCAGGCA
# AAGAATCAGTCA
# CAAGGAGTTCGC
# CACGTCAATCAC
# CAATAATATTCG
# print('\n'.join(greedy_motif_search(['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG'],3,5)))

# 3 4
# GCCCAA GGCCTG AACCTA TTCCTT
# print(greedy_motif_search(['GCCCAA','GGCCTG','AACCTA','TTCCTT'],3,4))
# print(greedy_motif_search_online(['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG'],3))

print('\n'.join(greedy_motif_search(dna,k,t)))