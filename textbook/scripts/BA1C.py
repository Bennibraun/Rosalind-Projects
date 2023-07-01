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

	with open(os.path.join(datapath,'rosalind_ba1c.txt')) as f:
		# read data
		dna = f.readline().strip()

def revc(dna):
	return ''.join([{'A':'T','T':'A','C':'G','G':'C'}[i] for i in dna])[::-1]

print(revc(dna))