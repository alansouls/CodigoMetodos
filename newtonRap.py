
# coding: utf-8

# In[ ]:


#import numpy as np
import sys

def newtonRap(f,fd,x0,e,maxIter):
    
    for i in range(0,maxIter):
        fi = lambda x: x - f(x)/fd(x)
        a = fi(x0)
        if a == x0:
            return x0
        if abs(f(a)) < e:
            return a
        x0 = a
        
    return x0

f = lambda x: eval(sys.argv[1])
fd = lambda x: eval(sys.argv[2])
x0 = float(eval(sys.argv[3]))
print(x0)
e = float(eval(sys.argv[4]))
print(e)
maxIter = 100
a = newtonRap(f,fd,x0,e,maxIter)
print(a)
