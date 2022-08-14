import numpy as np

lowerx = 0.001
upperx = 5
stepsize = 0.25
n = int(3)

F =[]
F.append(1)
F.append(1)
terms = 2
while terms<=n+1:
	F.append(F[terms-1]+F[terms-2]) 
	terms = terms + 1

print(F)

L = upperx - lowerx
#Lw = 1
a = lowerx
b = upperx
#stepsize = stepsize/L

cont = 1
global kfib
kfib = 2

while cont==1 and kfib<=n:

	
	print("ITERATION "+ str(kfib-1))
	print("a " + str(a))
	print("b " + str(b))
	if (n-kfib+1)>=0:
		Lk= (F[n-kfib+1]/F[n+1])*5
		print([n-kfib+1])
	else:
		print("Desired accuracy cannot be obtained, increase stepsize or n")
		cont = 0
		ans = [a, b]

	print("Lk  "+ str(Lk))

	kfib = kfib+1
	x1 = a + Lk
	x2 = b - Lk
	#xm = (a + b)/2
	
	print("x1 " + str(x1))
	print("x2 " + str(x2))
	#print("Iteration", i)
	
	f1 = x1**2 + 54/x1
	f2 = x2**2 + 54/x2
	#fxm = (xm*(upperx-lowerx) + lowerx)**2 + 54/(xm*(upperx-lowerx) + lowerx)
	print("f1 " + str(f1))
	print("f2 " + str(f2))
	

	if f1<=f2:
		#a = x1
		b = x2
		#xm = x1
		if np.abs(b-a)<=stepsize:
			ans = [a, b]
			print('here1')
			cont = 0

	else:

		if f1>f2:
			#b = x2
			a = x1
			#xm = x2
			if np.abs(b-a)<=stepsize:
				ans = [a, b]
				#print('here2')
				cont = 0
		else:
			a = x1
			b = x2

ans = [a,b]
print(ans)
# ansfinal = [(ans[0]*(upperx-lowerx) + lowerx), (ans[1]*(upperx-lowerx) + lowerx)]
# print(ansfinal)
print(kfib-1)