# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:03:20 2018

@author: Aluno
"""

import numpy as np
import sys


def calL(x,xArray,k):
    L = 1
    for i in range(xArray.size):
        if i != k:
            L *= (x - xArray[i])/(xArray[k] - xArray[i])
    return L
def interLa(x,fx,p):
    for i in range(p.size):
        f = 0
        for j in range(x.size):
            f += fx[j]*calL(p[i],x,j) 
        print('f('+str(p[i])+') = ',f)
    
        
    

x=np.array(np.mat(sys.argv[1]),dtype=float)
fx=np.array(np.mat(sys.argv[2]),dtype=float)
p = np.array(np.mat(sys.argv[3]),dtype=float)
print(x)
x = np.array(x[0])
fx = np.array(fx[0])
p = np.array(p[0])
interLa(x,fx,p)