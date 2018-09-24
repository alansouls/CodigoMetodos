
import numpy as np
import sys
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from timeit import default_timer as timer

def pontoFixo(f,fi,x0,e,maxIter):
    xlist = []
    for i in range(0,maxIter):
        a = fi(x0)
        xlist.append(x0)
        if a == x0:
            return x0,xlist
        if abs(f(a)) < e:
            return a,xlist
        x0 = a
        
    return x0,xlist

f = lambda x: eval(sys.argv[1])
fi = lambda x: eval(sys.argv[2])
x0 = float(eval(sys.argv[3]))
e = float(eval(sys.argv[4]))
maxIter = 100
start = timer()
a,xlist = pontoFixo(f,fi,x0,e,maxIter)
end = timer()
xarray = np.asarray(xlist)
fxarray = f(xarray)
flinarray = fi(xarray)
ilist = np.arange(0,len(xlist))
table = PrettyTable()
column_names = ['it','x0','f(x0)','phi(x0)','e']
table.add_column(column_names[0],ilist)
table.add_column(column_names[1],xarray)
table.add_column(column_names[2],fxarray)
table.add_column(column_names[3],flinarray)
table.add_column(column_names[4],[e]*len(xlist))
print(table.get_string(title = "Tabela do Metodo do Ponto Fixo :  " + sys.argv[1]))
print("RAIZ = ",a)
print("O algoritmo rodou em: "+ str((end - start)*1000) +  " milisegundos")
print("Iterações por milisegundos = " + str(len(xlist)/((end-start)*1000)))
x = np.arange(x0-5,x0+5,0.001)
plt.plot(x,f(x))
plt.plot(a,f(a),'r.',markersize = 10)
plt.title("Metodo do ponto fixo")
plt.show()
