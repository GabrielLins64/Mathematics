import matplotlib.pyplot as plt
import csv
from os.path import isfile
import numpy as np

def is_prime(x):
	if(x==1 or x==0): return False
	if(x==2): return True
	for i in range(2, int(x**(1/2))+1):
		if(x%i==0): return False
	return True

def discover_primes(initial, amount):
	primes = []
	for i in range(initial+1, initial+1+amount):
		if(is_prime(i)): primes.append(i)
	return primes

def is_csv_empty(path):
	with open(path) as f:
		lines = f.readlines()
	if(len(lines)==1): return True
	return False

def get_last_prime(path):
	with open(path) as f:
		lines = f.readlines()
	last = lines[-1].split(',') 
	return int(last[0]), int(last[1][:-1])

def get_primes(path):
	with open(path) as f:
		r = csv.reader(f, delimiter=',')
		lines = [int(row[1]) for row in r]
	# return lines[:int(len(lines)/2)]
	return np.array(lines)

def get_difference(path="primes.csv"):
	primes = get_primes(path)
	dif = []
	for i in range(1, len(primes)):
		dif.append(primes[i] - primes[i-1])
	return dif

def write_primes(amount, path="primes.csv"):
	print("Discovering primes, please wait...", end='\r')
	discovered, last_prime = 0, 0
	if((not isfile(path))): f = open(path, 'w')
	elif(is_csv_empty(path)): f = open(path, 'w')
	else:
		discovered, last_prime = get_last_prime(path)
		f = open(path, 'a')
	primes = discover_primes(last_prime, amount)
	with f:
		w = csv.writer(f)
		for num, elem in enumerate(primes, discovered+1):
			w.writerow([num, elem])
	print("Done!                             ")

def plot_difference(path="primes.csv"):
	y = np.array(get_difference(path))
	plt.yticks(np.arange(y.min(), y.max()+1, 1))
	plt.plot(y)
	plt.grid(axis='y', linestyle='-')
	plt.ylabel("Difference with its predecessor")
	plt.xlabel("Nth prime")
	plt.show()

def plot_primes(path="primes.csv"):
	y = get_primes(path)
	print("Number of discovered primes:", len(y))
	print("Last discovered prime:", y[-1])
	plt.plot(y)
	plt.ylabel("Primes")
	plt.xlabel("Nth prime")
	plt.show()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Execution:

# write_primes(1000)
# plot_primes()
# plot_difference()




