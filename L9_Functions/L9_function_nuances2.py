#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:42:24 2020

@author: ramanathanmuthuganapathy
"""
#To check whether function overloading works in Python
import random

def maxormin( min1 = True):
    print(lst1)
    print(id(lst1))
    y = sorted(lst1)
    val = y[0] if min1 else y[len(lst1)-1]
    return val

lst1 = [random.randint(10,100) for x in range(10)]
print(lst1)
print(id(lst1))
print('id of the function',id(maxormin))
y = maxormin()
print('min of the list is = ', y)

y = maxormin(False)
print('max of the list is = ', y)

def maxormin(x, min1 = True):
    print(lst1)
    print(id(lst1))
    y = sorted(x)
    val = y[0] if min1 else y[len(x)-1]
    return val

lst1 = [random.randint(10,100) for x in range(10)]
print(lst1)
print(id(lst1))
print('id of the function',id(maxormin))
y = maxormin(lst1)
print('min of the list is = ', y)

y = maxormin(lst1, False)
print('max of the list is = ', y)

#z = maxormin(False)