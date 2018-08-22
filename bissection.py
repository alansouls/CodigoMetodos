import math

def bissection(a,b,e,maxIter,f):
	if f(a) == 0:
		return a
	elif f(b) == 0:
		return b
	elif f(a)*f(b) > 0:
		return 'Erro'

	for i in range(0,maxIter):
		x = (b+a)/2
		if abs(b-a) < e:
			return x
		if f(x) == 0:
			return x
		if f(a)*f(x) < 0:
			b = x
		else:
			a = x

	return (b+a)/2


def functionTest(x):
	return pow(x,3)+pow(x,2)+x+2




r = bissection(-2.0,-1.0,0.0001,100,functionTest)
print(r)