
with open('data/rosalind_iev.txt') as f:
    genotypes = f.read().strip().split()
    genotypes = [int(g) for g in genotypes]

# genotypes = [1,0,0,1,0,1]
dom_probs = [1,1,1,0.75,0.5,0]

total = sum(genotypes)

expected = 0
for genotype, dom in zip(genotypes,dom_probs):
    expected += 2 * genotype * dom

print(expected)