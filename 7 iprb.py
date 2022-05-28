
with open('data/rosalind_iprb.txt','r') as f:
    k, m, n = f.readline().strip().split()
    k, m, n = int(k), int(m), int(n)

pop = k+m+n

prob_dominant = 1 - (m*n + .25*m*(m-1) + n*(n-1)) / (pop*(pop-1))

print(prob_dominant)
