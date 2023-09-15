if __name__ == '__main__':
	import os
	import glob

	datapath = []
	if 'textbook' in glob.glob('*'):
		datapath.append('textbook')
		datapath.append('data')
	elif len(glob.glob('*.py')) > 0:
		datapath.extend(['..','..','data'])
	datapath = os.path.join(*datapath)

	path = os.path.join(datapath,'rosalind_ba3a.txt')
	if os.path.exists(path):
		with open(path) as f:
			k = int(f.readline().strip())
			text = f.readline().strip()

def composition(text,k):
	kmers = [text[i:i+k] for i in range(len(text)-k+1)]
	return sorted(kmers)

# print(composition('CAATCCAAC',5))
print('\n'.join(composition(text,k)))