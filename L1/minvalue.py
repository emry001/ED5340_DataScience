#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:17:15 2020

@author: ramanathanmuthuganapathy
"""
"""
Program to demonstrate the find the min. of two values in Python

"""

#print(s)


# Returning the min of two values

def minvalue(a, b):
    if a < b: 
        return a
    else: 
        return b
    

a = 5.5
b = 6.77
print('first call to min', minvalue(a,b))

a = 5
b = 4
print('second call to min', minvalue(a,b))

