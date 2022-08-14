import numpy as np


lowerx = 1
upperx = 8
stepsize = 0.001

# f(x) = x**2 + 54/x
# f'= 2x - 54/(x**2)

# def funncdash1(x):
# 	f = 2*x - 54/(x**2)
# 	return f

# def funncdash2(x):
# 	f = 2 + (54*2)/(x**3)
# 	return f

def bm_funncdash1(x):
	return (funnc(x+bm_deltax(x)) - funnc(x - bm_deltax(x)))/(2*bm_deltax(x))

def bm_funncdash2(x):
	return (funnc(x+bm_deltax(x)) - 2*funnc(x) + funnc(x - bm_deltax(x)))/((bm_deltax(x))**2)

def funnc(x):
	f = x**2 + 54/x
	return f

def bm_deltax(x):
	if abs(x)>0.01:
		return 0.01*abs(x)
	else:
		return 0.0001

intialguess = 1

a = 2
b = 5
# such that f'(a)f'(b)<0

# fdash1 = nr_funncdash1(intialguess)

cont = 1
global k_bm
k_bm = 0
x1 = a
x2 = b

while cont==1:

	print("Iteration " + str(k_bm))
	
	z = (x1+x2)/2
	print(z)

	if abs(bm_funncdash1(z))<stepsize:
		ans = [x1,x2]
		cont = 0

	else:
		if bm_funncdash1(z)<0:
			x1  = z
		else:
			x2 =z

		k_bm = k_bm +1
			

print(ans)
