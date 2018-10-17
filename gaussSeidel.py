import sys 
import numpy as np


def checkMatrix(A):
	n = A.shape[0]
	for i in range(n):
		s = 0
		for k in range(n):
			if i != k:
				s += abs(A[i,k])
		if abs(A[i,i]) <= s:
			return False
	return True 