
# coding: utf-8

# In[ ]:


#import numpy as np
import sys

def newtonRap(f,x0,x1,e,maxIter):
    d = lambda x,y: (f(x) - f(y))/(x - y)
    for i in range(0,maxIter):
        fi = lambda x: x - f(x)/d(x1,x0)
        a = fi(x0)
        if a == x0:
            return x0
        if abs(f(a)) < e:
            return a
        x0 = a
        
    return x0

f = lambda x: eval(sys.argv[1])
x0 = float(eval(sys.argv[2]))
x1 = float(eval(sys.argv[3]))
e = float(eval(sys.argv[4]))

maxIter = 100
a = newtonRap(f,x0,x1,e,maxIter)
print(a)
