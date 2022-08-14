#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:21:01 2020

@author: ramanathanmuthuganapathy
"""


#Recursive function

def PrintNum(n):
    if n > 0:
        # print('Value of n before the function call', n)
        # print('mem. id of n is ', id(n))
        PrintNum(n-1) 
        print('Value of n after the function call', n)
    return n
    
PrintNum(3)

def sumofnterms(n):
    if n == 0:
        return 0
    else:
        #print(s) - Error
        s = n+sumofnterms(n-1)
        print(s)
    return s

s = sumofnterms(4)
print('Sum of n terms ', s)