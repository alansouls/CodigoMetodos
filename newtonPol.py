
# coding: utf-8

# In[ ]:


#import numpy as np
import sys

def newtonRap(coef,x0,e,maxIter):
    for i in range(0,maxIter):
        b,c = valorPol(coef,x0) 
        a = x0 - b/c
        if a == x0:
            return x0
        if abs(valorPol(coef,x0)[0]) < e:
            return a
        x0 = a
        
    return x0


def valorPol(coef,x):
    b = [coef[0]]
    c = [b[0]]
    for i in range(1,len(coef)):
        b.append(coef[i] + b[i-1]*x)
    for i in range(1,len(coef)-1):
        c.append(b[i] + c[i-1]*x)
    return b[-1],c[-1]



coef = list(eval(sys.argv[1]))
x0 = float(eval(sys.argv[2]))

e = float(eval(sys.argv[3]))

maxIter = 100
a = newtonRap(coef,x0,e,maxIter)
print(a)
