import sys 
import numpy as np
import solveTriang as sT
from timeit import default_timer as timer

def piv(A,b,l,p):
	n = A.shape[0]
	maximo,index = 0,l
	for i in range(l,n):
		if maximo < abs(A[i,l]):
			maximo,index = abs(A[i,l]),i
	if l!=index:
		A[[l,index]] = A[[index,l]]
		b[0,l],b[0,index] = b[0,index],b[0,l]
		p += 1
	return p


def gauss(A,b,pivot = True):
	p = 0
	print("A matriz A será convertida em matriz triangular: ")
	print("Matriz A: ")
	print(A)
	Aini = np.copy(A)
	print("Vetor b:")
	print(np.transpose(b))
	bini = np.copy(b)
	n = A.shape[0]
	start = timer()
	for k in range(0,n-1):
		print("Matriz nao pivotada :\n",A)
		if pivot == True:
			p = piv(A,b,k,p)
		print("Matriz pivotada em :", k)
		print(A)
		for i in range(k,n-1):
			m = (-1)*(A[i+1,k])/A[k,k]
			for j in range(k,n):
				A[i+1,j] = m*A[k,j] + A[i+1,j]
			b[0,i+1] = m*b[0,k] + b[0,i+1]
	end = timer()
	print("Tempo de execução do código: %e", (end-start))
	print("Tempo de execução por iteração: %e",(end-start)/n)

	print("Nova matriz A: ")
	print(A)
	print("Novo vetor b: ")
	print(np.transpose(b))
	det = 1

	for i in range(0,n):
		det *= A[i,i]
	x = sT.solveTriang(A,b,True,False)	
	x = x[:,None]
	if pivot == True:
		if(p % 2 != 0):
			det = -det
	print("Det A = ", det)
	print("RESIDUOS:\n",np.transpose(bini) - Aini@x)
	return x
A=np.array(np.mat(sys.argv[1]),dtype=float)
b=np.array(np.mat(sys.argv[2]),dtype=float)


print("Solução: \n",gauss(A,b))
