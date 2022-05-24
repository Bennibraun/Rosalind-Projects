from Bio import SeqIO

seqs = SeqIO.parse("data/rosalind_cons.txt", "fasta")

nt_map = {'A':[],'C':[],'G':[],'T':[]}

sized = False
for seq in seqs:
    if not sized:
        for key in nt_map:
            nt_map[key] = [0] * len(seq.seq)
        sized = True
    i = 0
    for nt in seq.seq:
        nt_map[nt][i] += 1
        i += 1

for row in range(len(nt_map['A'])):
    loc_map = {'A':nt_map['A'][row],'C':nt_map['C'][row],'G':nt_map['G'][row],'T':nt_map['T'][row]}
    max_nt = max(loc_map, key=loc_map.get)
    print(max_nt,end='')

print()

for key in nt_map:
    nt_map[key] = [str(x) for x in nt_map[key]]
    print(key+':',' '.join(nt_map[key]))
    