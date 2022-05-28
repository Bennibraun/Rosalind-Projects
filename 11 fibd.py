
with open('data/rosalind_fibd.txt','r') as f:
    n, m = f.readline().strip().split()
    n = int(n)
    m = int(m)

rabbits = [0]*m
rabbits[0] = 1
for i in range(n-1):
    temp = sum(rabbits[1:])
    rabbits = [temp] + rabbits[:-1]

print(sum(rabbits))

