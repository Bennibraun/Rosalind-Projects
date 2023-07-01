
with open('data/rosalind_subs.txt','r') as f:
    s = f.readline().strip()
    t = f.readline().strip()

locs = []
for i in range(len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        locs.append(str(i+1))

print(' '.join(locs))