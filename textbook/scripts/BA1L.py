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

	with open(os.path.join(datapath,'rosalind_ba1l.txt')) as f:
		# read data
		pattern = f.readline().strip()


def symbol_to_number(symbol):
	return {'A':0,'C':1,'G':2,'T':3}[symbol]

def pattern_to_number(pattern):
	if len(pattern) == 0:
		return 0
	symbol = pattern[-1]
	prefix = pattern[:-1]
	return 4*pattern_to_number(prefix) + symbol_to_number(symbol)

print(pattern_to_number(pattern))