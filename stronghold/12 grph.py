from Bio import SeqIO


with open('data/rosalind_grph.txt') as f:
    dna = SeqIO.parse(f, 'fasta')

    nodes = {}
    for record in dna:
        nodes[record.id] = str(record.seq)

k = 3

for s in nodes:
    suffix = nodes[s][-k:]
    for t in nodes:
        if nodes[t] != nodes[s]:
            prefix = nodes[t][:k]
            if suffix == prefix:
                print(s,t)