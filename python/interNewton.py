# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:17:56 2018

@author: Aluno
"""

import numpy as np
import sys


def fDiferenca(x,fx,xOri):
    
    if x.size == 1:
        return float(fx[np.where(xOri == x)[0]])
    else:
        x1 = x[0:x.size -1]
        x2 = x[1:x.size]
        return (fDiferenca(x2,fx,xOri) - fDiferenca(x1,fx,xOri))/(x[-1] - x[0])
def interNewton(x,fx,p):
    for i in range(p.size):
        f = fx[0]
        for j in range(1,x.size):
            a = 1
            for k in range(j):
                a*= (p[i]-x[k])
            f += a*fDiferenca(x[0:j+1],fx,x)
        print('f('+str(p[i])+') = ',f)
    
        
    

x=np.array(np.mat(sys.argv[1]),dtype=float)
fx=np.array(np.mat(sys.argv[2]),dtype=float)
p = np.array(np.mat(sys.argv[3]),dtype=float)
x = np.array(x[0])
fx = np.array(fx[0])
p = np.array(p[0])
interNewton(x,fx,p)