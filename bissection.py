import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sys
from prettytable import PrettyTable

def bissection(a,b,e,maxIter,f):
	xlist = []
	alist = []
	blist = []
	iList = []
	if f(a) == 0:
		
		return a,xlist,alist,blist,ilist
	elif f(b) == 0:
		
		return b,xlist,alist,blist,ilist
	elif f(a)*f(b) > 0:
		return 'Erro',xlist,alist,blist,ilist
	
	for i in range(0,maxIter):
		x = (b+a)/2
		xlist.append(x)
		alist.append(a)
		blist.append(b)
		iList.append(i)
		if abs(b-a) < e:
			return x,xlist,alist, blist, iList
		if f(x) == 0:
			return x,xlist,alist, blist, iList
		if f(a)*f(x) < 0:
			b = x
		else:
			a = x
		
	return (b+a)/2, xlist, alist, blist, iList

f = lambda x : eval(sys.argv[1])
a = float(sys.argv[2])
b = float(sys.argv[3])
e = float(sys.argv[4])
fig,ax = plt.subplots()
r, xlist, alist,blist,ilist = bissection(a,b,e,100,f)
x = np.arange(a,b,0.001)
xarray = np.asarray(xlist)
ln, =  ax.plot(xarray,f(xarray),'g.',markersize = 10)
textUpdate = ax.text(a + 0.1,f(b)- f(b)*0.3,"Iteração = " + str(0))
textUpdate2 = ax.text(a + 0.1,f(b) - f(b)*0.25,"X medio = " + str((a+b)/2))
ax.set_title("Método da bisseção para " + "$"+ sys.argv[1] + "$")
funcao, = ax.plot(x,f(x))
raiz, = ax.plot(r,f(r),'r.',markersize = 10)
ax.text(a + 0.1,f(b) - f(b)*0.3,"Valor da Raíz = " + str((r)))
ax.legend((funcao,raiz,ln),('Funcao','Raiz','X medio'),loc = 'lower right')

def init():
	f = lambda x : eval(sys.argv[1])
	a = float(sys.argv[2])
	b = float(sys.argv[3])
	ax.set_xlim(a,b)
	ax.set_ylim(f(a),f(b))
	return ln,textUpdate,textUpdate2,

def animationFunction(x):
	f = lambda x : eval(sys.argv[1])
	ln.set_xdata(x)
	ln.set_ydata(f(x))
	i, = np.where(xarray == x)
	textUpdate = ax.text(a + 0.1,f(b)-f(b)*0.1,"Iteração = " + str(i))
	textUpdate2 = ax.text(a + 0.1,f(b) - f(b)*0.2,"X medio = " + str(x))
	return ln,textUpdate,textUpdate2,



print(r)

table = PrettyTable(title = 'ola')

column_names = ['it','a','f(a)','b','f(b)','xm','f(xm)','e','b-a']
table.add_column(column_names[0],ilist)
table.add_column(column_names[1],alist)
table.add_column(column_names[2],f(np.asarray(alist)))
table.add_column(column_names[3],blist)
table.add_column(column_names[4],f(np.asarray(blist)))
table.add_column(column_names[5],xlist)
table.add_column(column_names[6],f(np.asarray(xlist)))
table.add_column(column_names[7],[e]*len(xlist))
table.add_column(column_names[8],np.asarray(blist) - np.asarray(alist))

print(table)
if r != 'erro':
	ani = animation.FuncAnimation(fig, animationFunction, frames=xarray,
                    init_func=init, blit=True)
	plt.show()
else:
	print(r)