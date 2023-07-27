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

	with open(os.path.join(datapath,'rosalind_ba1d.txt')) as f:
		# read data
		pattern = f.readline().strip()
		genome = f.readline().strip()


def pattern_match(pattern,genome):
	positions = []
	for i in range(len(genome)-len(pattern)+1):
		if genome[i:i+len(pattern)] == pattern:
			positions.append(i)
	return positions

print(' '.join([str(x) for x in pattern_match(pattern,genome)]))