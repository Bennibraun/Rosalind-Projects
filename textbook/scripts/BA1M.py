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

	with open(os.path.join(datapath,'rosalind_ba1m.txt')) as f:
		# read data
		number = int(f.readline().strip())
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

print(number_to_pattern(number,k))