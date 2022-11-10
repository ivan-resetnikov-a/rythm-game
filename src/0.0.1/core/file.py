from json import load


def get (filename) :
	with open(filename, 'r') as f :
		return load(f)