#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:28:55 2020

@author: ramanathanmuthuganapathy
"""


#To demonstrate variable names, arguments in functions 

#Sumof function

def sumof(a1, b1, c1):
    d = 10
    print('ids of a,b,c inside the function = ', id(a1), id(b1), id(c1))
    return (a1+b1+c1+d)/3

a, b, c = 3, 4, 5
print('ids of a,b,c = ', id(a), id(b), id(c))
print(sumof(a, b, c))

#print(d) # - d is local to the function and hence this st will show an error

def sumof1(i, j, k):
    i = 10
    print('ids of i,j,k inside the function = ', id(i), id(j), id(k))
    return i

a1, b1, c1 = 3, 4, 5
print('ids of a1,b1,c1 = ', id(a1), id(b1), id(c1))
print(sumof1(a1, b1, c1))
print('Changing i does not change a1', a1)

#Why the ids of a, b, c are same as a1, b1, c1? 


a2, b2, c2 = 4, 5, 7
print('ids of a2,b2,c2 = ', id(a2), id(b2), id(c2))
print(sumof1(a2, b2, c2))
#print(a1, b1, c1)
      
def sumof2():
    return (a2+b2)

print(sumof2())
