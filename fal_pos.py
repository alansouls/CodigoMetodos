import sys
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def fal_pos(a,b,e,f,maxIter = 100):
	if f(a) == 0:
		return a
	elif f(b) == 0:
		return b
	elif f(a)*f(b) > 0:
		return "erro"

	print("it\t a\t\t f(a)\t\t b\t\t f(b)\t\t x0\t\t f(x0)\t\t epsilon\t b-a\n")
	for i in range(0,maxIter):
		x0 = (a*f(b) - b*f(a))/(f(b)-f(a))
		print("%d\t %e\t %e\t %e\t %e\t %e\t %e\t %e\t %e\n"%(i,a,f(a),b,f(b),x0,f(x0),e,b-a))
		if f(x0) == 0:
			return x0
		elif abs(f(x0)) < e:
			return x0
		if f(a)*f(x0) < 0:
			b = x0
		else:
			a = x0
	return x0

print("",1.0)
f = lambda x:eval(sys.argv[1])
a = float(sys.argv[2])
b = float(sys.argv[3])
e = float(sys.argv[4])
r = fal_pos(a,b,e,f,)
print(r)
t = np.arange(1,3,0.001)
plt.plot(t,f(t))
plt.grid()
plt.annotate('Raiz da Equacao', xy =(r,0),xytext = (r,2),arrowprops=dict(facecolor='black', shrink=0.05),)
plt.show()