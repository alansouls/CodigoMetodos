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

def gaussJacobi(A,b,e,maxIter = 300):
	print("Matriz A:\n",A)
	print("Vetor b:\n",np.transpose(b))
	n = A.shape[0]
	x = np.zeros(b.shape)
	for i in range(0,n):
		x[0,i] = b[0,i]/A[i,i]
	print("Vetor X0 \n", np.transpose(x))
	xProx = np.copy(x)
	print("Verificando se a matriz obedece o critério das linhas...")
	if checkMatrix(A) == False:
		print("A matriz pode não convergir")
	else:
		print("A matriz possui diagonal estritamente dominante")
	C = np.copy(A)
	for i in range(n):
		C[i,i] = 0
		C[i] = -C[i]/A[i,i] 
	g = np.copy(b)
	for i  in range(n):
		g[0,i] = g[0,i]/A[i,i]
	aux = np.copy(x)
	for p in range(0,maxIter):
		x = aux
		print("XP\n",x)
		xProx = np.transpose(C @ np.transpose(x) + np.transpose(g))
		aux = np.copy(xProx)
		print("XS\n",x)
		d = abs(xProx - x)
		print("D\n",d)
		maxDR = np.amax(d)/np.amax(abs(x))
		if maxDR < e:
			break
	print("O vetor solução aproximado é \n", np.transpose(xProx))
	print("Numero de iterações: ", p)
	return xProx


A=np.array(np.mat(sys.argv[1]),dtype=float)
b=np.array(np.mat(sys.argv[2]),dtype=float)
e = float(sys.argv[3])
gaussJacobi(A,b,e,)
