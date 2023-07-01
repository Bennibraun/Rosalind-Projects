from Bio import SeqIO

dna = SeqIO.parse(open('data/rosalind_gc.txt', 'r'), 'fasta')

highest_gc = ('',0)
for fasta in dna:
    gc_count = 0
    for base in fasta.seq:
        if base == 'G' or base == 'C':
            gc_count += 1
    gc_count = (gc_count / len(fasta.seq)) * 100
    if gc_count > highest_gc[1]:
        highest_gc = (fasta.id, gc_count)

print(highest_gc[0],'\n'+str(highest_gc[1])[:-8])
