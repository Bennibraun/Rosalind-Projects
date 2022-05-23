

nt_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

with open('data/rosalind_dna.txt', 'r') as f:
    bases = f.readline().strip()
    # bases = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    for base in bases:
        nt_count[base] += 1

for key, value in nt_count.items():
    print(value,end=' ')