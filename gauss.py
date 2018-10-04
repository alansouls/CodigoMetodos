import sys 
import numpy as np
import solveTriang as sT

def gauss(A,b):
	print("A matriz A será convertida em matriz triangular: ")
	print("Matriz A: ")
	print(A)
	print("Vetor b:")
	print(np.transpose(b))
	n = A.shape[0]
	for k in range(0,n-1):
		for i in range(k,n-1):
			m = (-1)*(A[i+1,k])/A[k,k]
			for j in range(k,n):
				A[i+1,j] = m*A[k,j] + A[i+1,j]
			b[0,i+1] = m*b[0,k] + b[0,i+1]
	print("Nova matriz A: ")
	print(A)
	print("Novo vetor b: ")
	print(np.transpose(b))
	det = 0
	for i in range(0,n):
		det += A[i,i]
	x = sT.solveTriang(A,b,True,False)	
	x = x[:,None]
	print("Det A = ", det)
	return x
A=np.array(np.mat(sys.argv[1]),dtype=float)
b=np.array(np.mat(sys.argv[2]),dtype=float)


print("Solução: \n",gauss(A,b))
