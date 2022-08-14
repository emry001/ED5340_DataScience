#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:42:46 2020

@author: ramanathanmuthuganapathy
"""


#combining all types of arguments - pos, var. pos., kw, var. kw

#Positional and var. pos.
def pv(i, j, *args):
    print(i, j)
    for var in args:
        print(var)
        
pv(10, 23.56, 'Ram', 'Raj')

def pvk(*args, i, j):
    print(i, j)
    for var in args:
        print(var)
        
pvk('Ram', 'Raj', 10, 23.56) # *args before won't work. 
#pvk('Ram', 'Raj', i = 10, j = 23.56) # This will work as *args is followed by keyword arguments

def pvkv(i, j, *args, k, **kwargs):
    print(i, j)
    for var in args:
        print(var)
    print(k)
    for k, v in kwargs.items():
        print(k, v)
        
pvkv(10, 24.55, 'Ram', 'Raj', k = 567, l = 43, m = 56.67)

#default arguments
def printTorF(i, check = True):
    print('Parameter check\'s value is :', check)
    if check:
        print('Defalut value True')
    else:
        print('False')

print()
printTorF(5)
# printTorF(i = 10, False)
            

 