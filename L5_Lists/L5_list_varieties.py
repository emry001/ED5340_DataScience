#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:26:56 2020

@author: ramanathanmuthuganapathy
"""


# List varieties
# List of lists

a = [1,2,3,4,5]
b = [11,12,13,14,15]
c = [a, b]
print('list of lists',c)

#individual elements accessing - similar to 2D array
print('some list elements: ',c[0][0], c[1][0], c[0][4], c[1][4])

#You can also do the following
a = [1,2,3,4,5]
b = [11,12,13,14]
c = [a, b]
print('list of lists',c)

#What difference did you find from the above?
print('some list elements: ',c[0][0], c[1][0], c[0][4], c[1][3])

#List embedding
x = [1, 2, 3, 4]
y = [10, 11, x, 13]
print('Embedded list',y, type(y))

#List unpacking
x = [1, 2, 3, 4]
y = [10, 11, *x, 13]
print('Unpacked list',y, type(y))

s = 'Raman'
l = [*s]
print('unpacking of a string to a list', l)