import matplotlib.pyplot as plt
import numpy as np
import sys
from prettytable import PrettyTable
from timeit import default_timer as timer

def fal_pos(a,b,e,f,maxIter = 100):
	xlist = []
	alist = []
	blist = []
	ilist = []
	if f(a) == 0:
		return a,xlist,alist,blist,ilist
	elif f(b) == 0:
		return b,xlist,alist,blist,ilist
	elif f(a)*f(b) > 0:
		return None,None,None,None,None

	
	for i in range(0,maxIter):
		x0 = (a*f(b) - b*f(a))/(f(b)-f(a))
		xlist.append(x0)
		alist.append(a)
		blist.append(b)
		ilist.append(i)
		if f(x0) == 0:
			return x0,xlist,alist,blist,ilist
		elif abs(f(x0)) < e:
			return x0,xlist,alist,blist,ilist
		if f(a)*f(x0) < 0:
			b = x0
		else:
			a = x0
	return x0,xlist,alist,blist,ilist


f = lambda x:eval(sys.argv[1])
a = float(sys.argv[2])
b = float(sys.argv[3])
e = float(sys.argv[4])
start = timer()
r,xlist,alist,blist,ilist = fal_pos(a,b,e,f,)
end = timer()
table = PrettyTable(title = 'Metodo da Posição Falsa')
xlist = np.asarray(xlist)
alist = np.asarray(alist)
blist = np.asarray(blist)
ilist = np.asarray(ilist)

column_names = ['it','a','f(a)','b','f(b)','xi','f(xi)','e','b-a']
table.add_column(column_names[0],ilist)
table.add_column(column_names[1],alist)
table.add_column(column_names[2],f(np.asarray(alist)))
table.add_column(column_names[3],blist)
table.add_column(column_names[4],f(np.asarray(blist)))
table.add_column(column_names[5],xlist)
table.add_column(column_names[6],f(np.asarray(xlist)))
table.add_column(column_names[7],[e]*len(xlist))
table.add_column(column_names[8],np.asarray(blist) - np.asarray(alist))
print(r)
t = np.arange(1,3,0.001)
plt.plot(t,f(t))
plt.plot(r,f(r),'r.')
plt.title("Metodo da Posição Falsa")
print("O algoritmo rodou em: "+ str((end - start)*1000) +  " milisegundos")
print("Iterações por milisegundos = " + str(len(xlist)/((end-start)*1000)))
print(table)
plt.show()