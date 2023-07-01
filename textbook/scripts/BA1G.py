

if __name__ == '__main__':
	import os
	import glob

	datapath = []
	if 'textbook' in glob.glob('*'):
		datapath.append('textbook')
		datapath.append('data')
	elif len(glob.glob('*.py')) > 0:
		datapath.append('..')
		datapath.append('data')
	datapath = os.path.join(*datapath)

	with open(os.path.join(datapath,'rosalind_ba1g.txt')) as f:
		# read data
		p = f.readline().strip()
		q = f.readline().strip()


def hamming_distance(p,q):
	hamming = 0
	for i in range(len(p)):
		if p[i] != q[i]:
			hamming += 1
	return hamming

# p = 'GGGCCGTTGGT'
# q = 'GGACCGTTGAC'

print(hamming_distance(p,q))
