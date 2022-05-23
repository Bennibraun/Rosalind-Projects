

with open('data/rosalind_fib.txt','r') as f:
    n, k = f.readline().strip().split()
    n = int(n)
    k = int(k)

mature = 0
young = 1
for i in range(n):
    new_young = mature * k
    mature += young
    young = new_young

print(mature)
