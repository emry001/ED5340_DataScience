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

def nr_funncdash1(x):
	return (funnc(x+nr_deltax(x)) - funnc(x - nr_deltax(x)))/(2*nr_deltax(x))

def nr_funncdash2(x):
	return (funnc(x+nr_deltax(x)) - 2*funnc(x) + funnc(x - nr_deltax(x)))/((nr_deltax(x))**2)

def funnc(x):
	f = x**2 + 54/x
	return f

def nr_deltax(x):
	if abs(x)>0.01:
		return 0.01*abs(x)
	else:
		return 0.0001

intialguess = 1

a = lowerx
b = upperx

fdash1 = nr_funncdash1(intialguess)

cont = 1
global k_nr
k_nr = 0
x = [intialguess]

while cont==1:

	print("Iteration " + str(k_nr))
	print(x[k_nr])
	print(nr_funncdash1(x[k_nr]))
	x.append((x[k_nr] - (nr_funncdash1(x[k_nr])/nr_funncdash2(x[k_nr]))))

	if abs(nr_funncdash1(x[k_nr+1]))<stepsize:
		ans = x[k_nr+1]
		cont = 0

	else:
		k_nr = k_nr+1

print(ans)
