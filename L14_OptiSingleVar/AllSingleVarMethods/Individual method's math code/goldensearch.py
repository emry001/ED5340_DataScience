import numpy as np

lowerx = 0.1
upperx = 5
stepsize = 0.25

L = upperx - lowerx
#Lw = 1
a = 0
b = 1
#stepsize = stepsize/L

cont = 1
global kinthalf
kinthalf = 0

while cont==1:

	kinthalf = kinthalf+1
	print("ITERATION "+ str(kinthalf))
	print("b " + str(b))
	print("a " + str(a))
	Lw = b - a
	print("Lw  "+ str(Lw))
	x1 = a + Lw*0.618
	x2 = b - Lw*0.618
	#xm = (a + b)/2
	
	print("w1" + str(x1))
	print("w2" + str(x2))
	#print("Iteration", i)
	
	f1 = (x1*(upperx-lowerx) + lowerx)**2 + 54/(x1*(upperx-lowerx) + lowerx)
	f2 = (x2*(upperx-lowerx) + lowerx)**2 + 54/(x2*(upperx-lowerx) + lowerx)
	#fxm = (xm*(upperx-lowerx) + lowerx)**2 + 54/(xm*(upperx-lowerx) + lowerx)
	print("f1" + str(f1))
	print("f2" + str(f2))
	

	if f1<=f2:
		a = x2
		#xm = x1
		if np.abs(b-a)<=stepsize:
			ans = [a, b]
			print('here1')
			cont = 0

	else:

		if f1>f2:
			b = x1
			#xm = x2
			if np.abs(b-a)<=stepsize:
				ans = [a, b]
				#print('here2')
				cont = 0
		else:
			a = x1
			b = x2

print(ans)
ansfinal = [(ans[0]*(upperx-lowerx) + lowerx), (ans[1]*(upperx-lowerx) + lowerx)]
print(ansfinal)