# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:14:32 2018

@author: Aluno
"""
import numpy as np
import sys
import gauss as g

def interSisLinear(x,fx,p):
    x = np.vander(x,increasing = True)
    a = g.gauss(x,fx,True)
    s = ''
    print(a)
    n = a.shape[0]
    for i in range(n):
        if i > 0:
            s += str(a[i])+'*x^'+str(i)
        else:
            s += str(a[i])
        s += ' '
    print('Polinomio interpolador é '+s)
    for i in range(p.size):
        f = 0
        for j in range(a.shape[0]):
            f += a[j,0]*(p[i]**j) 
        print('f('+str(p[i])+') = ',f)
        
    

x=np.array(np.mat(sys.argv[1]),dtype=float)
fx=np.array(np.mat(sys.argv[2]),dtype=float)
p = np.array(np.mat(sys.argv[3]),dtype=float)
print(x)
x = np.array(x[0])
p = np.array(p[0])
interSisLinear(x,fx,p)