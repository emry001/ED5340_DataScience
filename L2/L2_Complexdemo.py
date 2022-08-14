#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:59:49 2020

@author: ramanathanmuthuganapathy
"""
# To demonstrate member function in `complex object'
#use of complex

a=1+2j
b=3*(1+2j)
c=a**b
print(a)
print(b)
print(c)
#Data and Member functions
print(a.real) # Data 'real'
print(a.imag) # Data 'imag'
print(a.conjugate()) #member function - returns complex conjugate

help(complex)