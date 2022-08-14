import numpy as np 

lowerx = 1
upperx = 8
stepsize = 0.5
intialguess = 1
param1 = 0.001
param2 = 0.001

cont = 1
cont2 = 1
global k_cs
k_cs = 0
# x1 = a
# x2 = b

def cs_funncdash1(x):
    return (funnc(x+cs_deltax(x)) - funnc(x - cs_deltax(x)))/(2*cs_deltax(x))

def cs_funncdash2(x):
    return (funnc(x+cs_deltax(x)) - 2*funnc(x) + funnc(x - cs_deltax(x)))/((cs_deltax(x))**2)

def funnc(x):
    f = x**2 + 54/x
    return f

def cs_deltax(x):
    if abs(x)>0.01:
        return 0.01*abs(x)
    else:
        return 0.0001

def cs_xbar(x1, x2):
    z = ((3*(funnc(x1)-funnc(x2)))/(x2-x1)) + cs_funncdash1(x1) + cs_funncdash1(x2)
    w = ((x2-x1)/(abs(x2-x1)))*np.sqrt(z**2 - (cs_funncdash1(x1)*cs_funncdash1(x2)))
    mu = (cs_funncdash1(x2) + w -z)/(cs_funncdash1(x2)-cs_funncdash1(x1) + 2*w)

    if mu == 0:
        xbar = x2
    else:
        if mu>1:
            xbar = x1
        else:
            xbar =  x2 - mu*(x2-x1)

    return xbar

delta = stepsize
if cs_funncdash1(intialguess)>0:
    delta = -1*delta

x = [intialguess]

while cont==1 and cont2==1:

    print(k_cs)
    print(x)

  #step2
    x.append((x[k_cs]) + (2**k_cs)*delta)

    if (cs_funncdash1(x[k_cs + 1]))*(cs_funncdash1(x[k_cs]))<=0:
        # print('yes')
        x1 = x[k_cs]
        x2 = x[k_cs+1]
        # print(x2)

        while cont2 == 1:

        #step 4
            xbar = cs_xbar(x1,x2)           
            # print(xbar)

        # step 5
            if funnc(xbar)<=funnc(x1):

          # step 6
                if (abs(cs_funncdash1(xbar))<=param1) and (abs((xbar-x1)/xbar)<=param2):
                    ans = [x1, x2]
                    cont = 0
                    cont2 = 0
                else:
                    if cs_funncdash1(xbar)*cs_funncdash1(x1)<0:
                        x2 = xbar
                    else:
                        x1 = xbar
            else:

                #while funnc(xbar)>funnc(x1):
                xbar = xbar - 0.5*(xbar - x1)
     
        # step 6
                if (abs(cs_funncdash1(xbar))<=param1) and (abs((xbar-x1)/xbar)<=param2):
                    ans = [x1, x2]
                    cont = 0
                    cont2 = 0
                else:
                    if cs_funncdash1(xbar)*cs_funncdash1(x1)<0:
                        x2 = xbar
                    else:
                        x1 = xbar

        #print(x1)
        #print(x2)

    else:
        k_cs = k_cs + 1


print(ans)


