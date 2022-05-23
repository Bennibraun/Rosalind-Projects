
with open('data/rosalind_rna.txt','r') as f:
    t = f.readline().strip()
    r = t.replace('T','U')
    print(r)