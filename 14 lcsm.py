from Bio import SeqIO

with open('data/rosalind_lcsm.txt','r') as f:
    dna = SeqIO.parse(f, 'fasta')
    dna = [str(dna.seq) for dna in dna]


def common_substr(s, seqs, length):
    for start in range(len(s)-length):
        substr = s[start:start+length]
        i = 0
        while i < len(seqs) and substr in seqs[i]:
            i += 1
        if i == len(seqs):
            return substr
    return None

longest_seq = max(dna, key=len)
length = 1
while True:
    if new_motif := common_substr(longest_seq, dna, length):
        motif = new_motif
    else:
        break
    length += 1

print(motif)
    
