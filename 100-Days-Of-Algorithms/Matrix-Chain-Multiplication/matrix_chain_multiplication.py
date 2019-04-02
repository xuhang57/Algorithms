# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n 
import sys

def MatrixChainMultiplication(matrices):
	n = len(matrices)
	# cost is zero when multiplying one matrix
	T = [[0 for _ in range(n)] for _ in range(n)]
	for l in range(2, n):
		for i in range(0, n-l):
			j = i + l
			T[i][j] = sys.maxsize
			for k in range(i+1, j):
				tmp = T[i][k] + T[k][j] + matrices[i] * matrices[k] * matrices[j]
				if tmp < T[i][j]:
					T[i][j] = tmp
	return T[0][-1]



if __name__ == '__main__':
	matrices = [4, 2, 3, 5, 3]
	# 84
	print(MatrixChainMultiplication(matrices))
