import numpy as np
import data_manipulation as dm

# Elementary operations:
# ---------------------------------------
def M(vec, line, scalar): # Multiplication by scalar
	vec[line] = vec[line]*scalar

def P(vec, l1, l2): # Permutation
	tmp = vec[l1].copy()
	vec[l1] = vec[l2].copy()
	vec[l2] = tmp

def E(vec, l2, l1, scalar): # Linear combination
	vec[l2] += vec[l1]*scalar
# ---------------------------------------

# Gauss Elimination:
# ---------------------------------------
def gauss_elimination(matrix, vector):
	A = matrix.copy()
	b = vector.copy()
	m, n = A.shape
	for j in range(0, n): # Escalonating
		for i in range(j+1, m):
			mul = A[i][j]/A[j][j] # Multiplier
			E(A, i, j, -mul)
			E(b, i, j, -mul)
	x = np.zeros(n)
	x[n-1] = b[n-1]/A[n-1][n-1] # Resolution
	for k in range(n-2, -1, -1):
		s = 0
		for j in range(k+1, n):
			s += A[k][j]*x[j]
		x[k] = (b[k] - s)/A[k][k]
	return x

def gauss_elimination_pivoting(matrix, vector):
	A = matrix.copy()
	b = vector.copy()
	m, n = A.shape
	for j in range(0, n):
		pivotLine = j # Pivoting
		for i in range(j+1, m):
			if(abs(A[i][j])>abs(A[pivotLine][j])):
				pivotLine = i
		P(A, j, pivotLine)
		P(b, j, pivotLine)
		for i in range(j+1, m): # Escalonating
			mul = A[i][j]/A[j][j] # Multiplier
			E(A, i, j, -mul)
			E(b, i, j, -mul)
	x = np.zeros(n)
	x[n-1] = b[n-1]/A[n-1][n-1] # Resolution
	for k in range(n-2, -1, -1):
		s = 0
		for j in range(k+1, n):
			s += A[k][j]*x[j]
		x[k] = (b[k] - s)/A[k][k]
	return x

def gauss_jordan(matrix, vector):
	A = matrix.copy()
	b = vector.copy()
	m, n = A.shape
	for j in range(0, n):
		for i in range(j+1, m): # Escalonating down
			mul = A[i][j]/A[j][j]
			E(A, i, j, -mul)
			E(b, i, j, -mul)
		for i in range(j-1, -1, -1): # Escalonating up
			mul = A[i][j]/A[j][j]
			E(A, i, j, -mul)
			E(b, i, j, -mul)
		M(b, j, 1/A[j][j]) # First do the below step in b, once A[j][j] will be modified next.
		M(A, j, 1/A[j][j]) # Making pivot equal to 1
	return b
# ---------------------------------------

# Useful methods:
# ---------------------------------------
def pivoting_need(matrix):
	n = min(matrix.shape)
	for i in range(0, n):
		if(abs(matrix[i][i])<0.0001):
			return True
	return False
# ---------------------------------------


a = dm.load('a4')
b = dm.load('b4')
print('A:\n', a)
print('b: ' + str(b))
x = gauss_jordan(a, b)
print('gj: ' + str(x))
piv = pivoting_need(a)
print('pivoting need: ' + str(piv))