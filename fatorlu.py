import sys 
import numpy as np
import solveTriang as sT


def piv(A,l,p):
	n = A.shape[0]
	maximo,index = 0,l
	for i in range(l,n):
		if maximo < abs(A[i,l]):
			maximo,index = abs(A[i,l]),i
	if l!=index:
		A[[l,index]] = A[[index,l]]
		p += 1
	return p


def fatorLU(A,b):
	p = 0
	print("Matriz A é :\n", A)
	print("Vetor b é :\n", np.transpose(b))
	n = A.shape[0]
	L = np.identity(n)
	U = A
	for k in range(0,n):
		#p = piv(U,k,p)
		for i in range(k,n-1):
			m = -U[i+1,k]/U[k,k]
			U[i+1] += U[k]*m
			L[i+1,k] = -m
	print("Matriz U:\n", U)
	print("Matriz L:\n", L)
	y = sT.solveTriang(L,b,False,False)
	y = y.reshape(1,n)
	print("Vetor y:\n", np.transpose(y))
	x = sT.solveTriang(U,y,True,False)
	x = x.reshape(1,n)
	print("TESTE : \n", L @ U)
	det = 1
	for i in range(0,n):
		det *= U[i,i]
	det *= (-1**p)
	print("Det de A = ", det)
	print("Vetor solução: \n",np.transpose(x))
	print("Vetor resíduos:\n", L@np.transpose(y) - np.transpose(b))


A=np.array(np.mat(sys.argv[1]),dtype=float)
b=np.array(np.mat(sys.argv[2]),dtype=float)

fatorLU(A,b)