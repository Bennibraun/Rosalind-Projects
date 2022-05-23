
with open('data/rosalind_revc.txt','r') as f:
    s = f.readline().strip()
    s_c = s[::-1]
    for bp in s_c:
        if bp == 'A':
            print('T',end='')
        elif bp == 'T':
            print('A',end='')
        elif bp == 'C':
            print('G',end='')
        elif bp == 'G':
            print('C',end='')
        else:
            print(bp,end='')