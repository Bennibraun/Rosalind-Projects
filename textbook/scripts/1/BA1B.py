from BA1A import pattern_count

def frequent_words(text,k):
	frequent_patterns = set()
	count = {}
	for i in range(len(text) - k + 1):
		pattern = text[i:i+k]
		count[i] = pattern_count(text,pattern)
	max_count = max(count.values())
	for i in range(len(text) - k + 1):
		if count[i] == max_count:
			frequent_patterns.add(text[i:i+k])
	return frequent_patterns

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

	with open(os.path.join(datapath,'rosalind_ba1b.txt')) as f:
		# read data
		text = f.readline().strip()
		k = int(f.readline().strip())


	result = frequent_words(text,k)
	print(' '.join(result))