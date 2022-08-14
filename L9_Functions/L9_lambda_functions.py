#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:22:22 2020

@author: ramanathanmuthuganapathy
"""

#Lambda functions
q = lambda x,y : print('sum = ', x+y)
print(q(3,5))

r = lambda x,y : x * y
print(r(4,5))

print((lambda s : s.upper())('Raman'))

avg = lambda a, b : (a+b) / 2
print(avg(avg(20,40),30))
print(avg(100,245.6))

#Higher order functions - a function that can receive other functions
dc1 = {'oil' : 3, 'stud' : 1, 'abc' : 2}
dc2 = sorted(dc1.items(), key = lambda kv1 : kv1[1])
print(dc2)

tup = ((0, 'Raman'), (213, 'Anand'), (40, 'Sid'), (50, 'Bits'))
tup1 = sorted(tup, key = lambda kv1 : kv1[1])
print(tup1)

#Functions as first class values

def f():
    return 10

def sum1(a,b,f):
    return print('sum =',a+b+f())

f1 = sum1
print(f1)
f1(10, 20, f)
