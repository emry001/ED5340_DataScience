import numpy as np


lowerx = 1
upperx = 8
stepsize = 0.001

a = lowerx
b = upperx

L = upperx - lowerx

# f(x) = x**2 + 54/x
# f'= 2x - 54/(x**2)

cont = 1
global kinthalf
kinthalf = 0

while cont==1:

	kinthalf = kinthalf+1
	x1 = lowerx + L/4
	x2 = upperx - L/4
	xm = (upperx + lowerx)/2
	#print("Iteration", i)
	
	f1 = x1**2 + 54/x1
	f2 = x2**2 + 54/x2
	fxm = xm**2 + 54/xm	
	print(f1)
	print(f2)

	if f1<=fxm:
		upperx = xm
		xm = x1
		if np.abs(upperx-lowerx)<=stepsize:
			ans = [lowerx, upperx]
			print('here1')
			cont = 0

	else:

		if f2<=fxm:
			lowerx = xm
			xm = x2
			if np.abs(upperx-lowerx)<=stepsize:
				ans = [lowerx, upperx]
				print('here2')
				cont = 0
		else:
			lowerx = x1
			upperx = x2


print(ans)
print(kinthalf)