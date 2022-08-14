#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 17:05:25 2021

@author: ramanathanmuthuganapathy
"""


#Function as value

def fun():
    print(1)
    return 10
    
f = fun #Assigning a function (this also calls the function)
f() # calling the function using assigned identifier

#Function as argument to another function
def sum(a, b, f):
    return a + b + f();
    
#Passing a function as argument 
print(sum(5, 6, f))

print('chr = ', chr(27))