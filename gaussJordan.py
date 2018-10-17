import sys 
import numpy as np

def piv(A,b,l,p = 0):
	n = A.shape[0]
	maximo,index = 0,l
	for i in range(l,n):
		if maximo < abs(A[i,l]):
			maximo,index = abs(A[i,l]),i
	if l!=index:
		A[[l,index]] = A[[index,l]]
		b[0,l],b[0,index] = b[0,index],b[0,l]
		p += 1
	return A

def gaussJordan(A,b):
	print("Matriz A é :\n",A)
	A0  = A
	print("Vetor b é : \n",np.transpose(b))
	b0 = b
	n = A.shape[0]
	I = np.zeros(A.shape)
	for i in range(0,n):
		I[i,i] = 1
	AI = np.array([A,I])
	for i in range(0,n):
		A = piv(AI[0],b,i)
		AI[0] = A
		b[0,i] /= AI[0,i,i]
		AI[:,i] = AI[:,i]/AI[0,i,i] 
		for k in range(0,n):
			if k != i:
				m = -AI[0,k,i]/AI[0,i,i]
				AI[:,k] += AI[:,i]*m
				b[0,k] += b[0,i]*m
	print("A nova matriz A é: \n",AI[0])
	print("A inversa de A é : \n",AI[1])
	print("O vetor solução x é : \n",np.transpose(b))
	print("O vetor de residuos é: \n",(A0.dot(np.transpose(b)))-np.transpose(b0))
	return b







A=np.array(np.mat(sys.argv[1]),dtype=float)
b=np.array(np.mat(sys.argv[2]),dtype=float)

gaussJordan(A,b)