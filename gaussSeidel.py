import sys 
import numpy as np
from timeit import default_timer as timer


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

def checkSassenfeld(A):
    b = np.zeros(A.shape[0])
    for i in range(0,A.shape[0]):
        s = 0
        for j in range(0,A.shape[0]):
            if i != j:
                if j < i:
                    s += abs(A[i,j])*b[j]
                else:
                    s += abs(A[i,j])
        b[i] = s/A[i,i]
    
    if np.amax(b) < 1:
        return True
    return False
def gaussSeidel(A,b,e,maxIter = 300):
    print("Matriz A:\n",A) 
    it = 0
    print("Vetor b:\n",np.transpose(b))
    n = A.shape[0]
    x = np.zeros(b.shape)
    print("Vetor X0 \n", np.transpose(x))
    print("Verificando se a matriz obedece o critério das linhas...")
    if checkMatrix(A) == False:
        print("A matriz pode não convergir")
    else:
        print("A matriz possui diagonal estritamente dominante")
    print("Verificando se a matriz obedece o critério de Sassenfeld...")
    if checkSassenfeld(A) == False:
        print("A matriz pode não convergir")
    else:
        print("A matriz obedece o critério de Sassenfeld")

    start = timer()
    for p in range(0,maxIter):
         it += 1
         xAnt = np.copy(x)
         for i in range(0,n):
             s = b[0,i]
             for k in range(0,n):
                 if(i != k):
                     s -= A[i,k]*x[0,k]
             x[0,i] = s/A[i,i]
         d = abs(x - xAnt)
         print("D\n",d)
         maxDR = np.amax(d)/np.amax(abs(x))
         if maxDR < e:
              break 
    end = timer()
    print("Tempo de execução do código: %e", (end-start))
    print("Tempo de execução por iteração: %e",(end-start)/it)       
    print("O vetor solução aproximado é \n", np.transpose(x))
    print("Numero de iterações: ", it)
    print("O vetor de residuos é: \n",np.transpose(b) - A@np.transpose(x))
    return x


A=np.array(np.mat(sys.argv[1]),dtype=float)
b=np.array(np.mat(sys.argv[2]),dtype=float)
e = float(sys.argv[3])
gaussSeidel(A,b,e,)
