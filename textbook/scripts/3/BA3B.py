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

	path = os.path.join(datapath,'rosalind_ba3b.txt')
	if os.path.exists(path):
		with open(path) as f:
			kmers = [line.strip() for line in f.readlines()]


def genome_path(kmers):
	text = kmers[0]
	for kmer in kmers[1:]:
		text += kmer[-1]
	return text

# print(genome_path(['ACCGA','CCGAA','CGAAG','GAAGC','AAGCT']))
print(genome_path(kmers))