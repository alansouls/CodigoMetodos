# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:53:30 2018

@author: Aluno
"""

import numpy as np
import sys
import gauss as g

def interInversa(x,fx,p):
    x = np.vander(x,increasing = True)
    a = g.gauss(x,fx,True)
    s = ''
    print(a)
    for i in range(p.size):
        print('Para f(x) = ',p[i])
        
    

x=np.array(np.mat(sys.argv[1]),dtype=float)
fx=np.array(np.mat(sys.argv[2]),dtype=float)
p = np.array(np.mat(sys.argv[3]),dtype=float)
print(x)
x = np.array(x[0])
p = np.array(p[0])
interInversa(x,fx,p)