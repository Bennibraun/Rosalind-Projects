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

	with open(os.path.join(datapath,'rosalind_ba1k.txt')) as f:
		# read data
		genome = f.readline().strip()
		k = int(f.readline().strip())


def number_to_symbol(number):
	return {0:'A',1:'C',2:'G',3:'T'}[number]

def number_to_pattern(index,k):
	if k == 1:
		return number_to_symbol(index)
	prefix_index = index // 4
	r = index % 4
	symbol = number_to_symbol(r)
	prefix_pattern = number_to_pattern(prefix_index,k-1)
	return prefix_pattern + symbol

def frequency_array(genome,k):
	kmers = []
	for i in range(len(genome)-k+1):
		pattern = genome[i:i+k]
		kmers.append(pattern)
	
	all_kmers = [number_to_pattern(x,k) for x in range(4**k)]
	freqs= {kmer:0 for kmer in all_kmers}
	for kmer in kmers:
		freqs[kmer] += 1
	# sort freqs by key lexicographically
	freqs = sorted(freqs.items(),key=lambda x: x[0])
	return freqs

print(' '.join([str(x[1]) for x in frequency_array(genome,k)]))