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

def sec_funncdash1(x):
	return (funnc(x+sec_deltax(x)) - funnc(x - sec_deltax(x)))/(2*sec_deltax(x))

def sec_funncdash2(x):
	return (funnc(x+sec_deltax(x)) - 2*funnc(x) + funnc(x - sec_deltax(x)))/((sec_deltax(x))**2)

def funnc(x):
	f = x**2 + 54/x
	return f

def sec_deltax(x):
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
global k_sec
k_sec = 0
x1 = a
x2 = b

while cont==1:

	print("Iteration " + str(k_sec))
	
	z = x2 - ((sec_funncdash1(x2))/((sec_funncdash1(x2)-sec_funncdash1(x1))/(x2-x1)))
	print(z)

	if abs(sec_funncdash1(z))<stepsize:
		ans = [x1,x2]
		cont = 0

	else:
		if sec_funncdash1(z)<0:
			x1  = z
		else:
			x2 =z
		k_sec = k_sec + 1
			

print(ans)
