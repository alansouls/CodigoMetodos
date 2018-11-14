# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:37:36 2018

@author: Aluno
"""

import sys 
import numpy as np
import solveTriang as sT
from timeit import default_timer as timer

def piv(A,b,l,p):
	n = A.shape[0]
	maximo,index = 0,l
	for i in range(l,n):
		if maximo < abs(A[i,l]):
			maximo,index = abs(A[i,l]),i
	if l!=index:
		A[[l,index]] = A[[index,l]]
		b[0,l],b[0,index] = b[0,index],b[0,l]
		p += 1
	return p


def gauss(A,b,pivot = True):
	p = 0
	
	
	Aini = np.copy(A)
	
	
	bini = np.copy(b)
	n = A.shape[0]
	start = timer()
	for k in range(0,n-1):
		
		if pivot == True:
			p = piv(A,b,k,p)
		
		
		for i in range(k,n-1):
			m = (-1)*(A[i+1,k])/A[k,k]
			for j in range(k,n):
				A[i+1,j] = m*A[k,j] + A[i+1,j]
			b[0,i+1] = m*b[0,k] + b[0,i+1]
	end = timer()
	

	
	det = 1

	for i in range(0,n):
		det *= A[i,i]
	x = sT.solveTriang(A,b,True,False)	
	x = x[:,None]
	if pivot == True:
		if(p % 2 != 0):
			det = -det
	
	return x