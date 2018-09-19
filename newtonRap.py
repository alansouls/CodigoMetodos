
# coding: utf-8

# In[ ]:


import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from prettytable import PrettyTable

def newtonRap(f,fd,x0,e,maxIter):
    xlist = []
    for i in range(0,maxIter):
        xlist.append(x0)
        fi = lambda x: x - f(x)/fd(x)
        a = fi(x0)
        if a == x0:
            return x0,xlist
        if abs(f(a)) < e:
            return a,xlist
        x0 = a
    
    return x0,xlist

def init():
	f = lambda x : eval(sys.argv[1])
	x0 = float(eval(sys.argv[3]))
	ax.set_xlim(x0-5,x0+5)
	ax.set_ylim(-5,5)
	return ln,textUpdate,textUpdate2,

def animationFunction(x):
	f = lambda x : eval(sys.argv[1])
	ln.set_xdata(x)
	ln.set_ydata(f(x))
	i, = np.where(xarray == x)
	textUpdate = ax.text(xLim[0] + 0.1,-f(xLim[-1])*0.1,"Iteração = " + str(i))
	textUpdate2 = ax.text(xLim[0] + 0.1,f(xLim[-1]) - f(xLim[-1])*0.2,"X0 = " + str(x))
	return ln,textUpdate,textUpdate2,

f = lambda x: eval(sys.argv[1])
fd = lambda x: eval(sys.argv[2])
x0 = float(eval(sys.argv[3]))
e = float(eval(sys.argv[4]))
maxIter = 100
a, xlist  = newtonRap(f,fd,x0,e,maxIter)
fig,ax = plt.subplots()
xLim = np.arange(x0-5,x0+5,0.001)
print(xLim[-1])
xarray = np.asarray(xlist)
ln, = ax.plot(xarray,f(xarray),'g.',markersize = 10)
textUpdate = ax.text(xLim[0] + 0.1,f(xLim[-1])- f(xLim[-1])*0.1,"Iteração = " + str(0))
textUpdate2 = ax.text(xLim[0] + 0.1,f(xLim[-1])- f(xLim[-1])*0.25,"X0 = " + str(x0))
ax.set_title("Método de newton para " + "$"+ sys.argv[1] + "$")

funcao, = ax.plot(xLim,f(xLim))
raiz, = ax.plot(a,f(a),'r.',markersize = 10)
ax.legend((funcao,raiz,ln),('Funcao','Raiz','X0'),loc = 'lower right')
fxarray = f(xarray)
flinarray = fd(xarray)
ilist = np.arange(0,len(xlist))
table = PrettyTable()
column_names = ['it','x0','f(x0)','f\'(x0)','e']
table.add_column(column_names[0],ilist)
table.add_column(column_names[1],xarray)
table.add_column(column_names[2],fxarray)
table.add_column(column_names[3],flinarray)
table.add_column(column_names[4],[e]*len(xlist))
print(table.get_string(title = "Tabela para o método de newton para " + sys.argv[1]))
print(a)
ani = animation.FuncAnimation(fig, animationFunction, frames=xarray,
                    init_func=init, blit=True)
plt.show()








