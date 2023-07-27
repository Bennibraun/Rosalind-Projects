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

	with open(os.path.join(datapath,'rosalind_ba1f.txt')) as f:
		# read data
		genome = f.readline().strip()


def minimum_gc_skew(genome):
	skew = 0
	mins = {'min':0,'indices':[]}
	for i,nuc in enumerate(genome):
		skew += {'G':1,'C':-1,'A':0,'T':0}[nuc]
		if skew < mins['min']:
			mins['min'] = skew
			mins['indices'] = [i+1]
		elif skew == mins['min']:
			mins['indices'].append(i+1)
	print(mins)
	return mins['indices']

# genome='CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG'

print(' '.join([str(x) for x in minimum_gc_skew(genome)]))