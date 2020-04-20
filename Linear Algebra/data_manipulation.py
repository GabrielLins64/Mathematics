import numpy as np

def load(name):
	directory = 'data/' + name
	v = np.loadtxt(directory)
	return v

def save(vec, name):
	directory = 'data/' + name
	np.savetxt(directory, vec, fmt='%.3f')