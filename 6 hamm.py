with open('data/rosalind_hamm.txt','r') as f:
    s1 = f.readline().strip()
    s2 = f.readline().strip()

hamming_distance = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        hamming_distance += 1

print(hamming_distance)