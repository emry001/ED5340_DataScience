#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 00:06:23 2021

@author: ramanathanmuthuganapathy
"""

#Multidimensional array and slicing
#Numpy ndarray is aliased as array
# https://numpy.org/doc/stable/user/quickstart.html

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim, a.shape, a.size, a.dtype, a.itemsize, a.data)
print(b.ndim, b.shape, b.size, b.dtype, b.itemsize, b.data)
print(c.ndim, c.shape, c.size, c.dtype, c.itemsize, c.data)
print(d.ndim, d.shape, d.size, d.dtype, d.itemsize, d.data)

e = np.arange(15).reshape(3, 5)
print(c, e)
print(len(b))
#Printing 1D array
for i in range(len(b)):
    print(b[i])

print('Print the 2D array with two for loops')
for i in range(len(c)):
    for j in range(len(c[0])):
        print(c[i, j])
        
#Trying using comprehension
print('Printing the 2D array using comprehension: Hey it works!')
[print(c[i, j]) for i in range(len(c)) for j in range(len(c[0]))]

#Using negative index to print
print(c[1, -1])

#Slicing [start:end:step]

print(b[1:3], b[0:], b[:9], b[-3:-1:2], b[0::2])

#using zeros and ones
zeros = np.zeros((3,5))
print(zeros)

ones = np.ones((2,3,4))
print(ones)

emp = np.empty((4,6))
print(emp)

# arange in array
ran = np.arange(1, 5, 0.5)
print(ran, type(ran))

from numpy import pi
x = np.linspace(0, 2, 9)
print(x)
x = np.linspace(0, 2*pi, 100)
y = np.sin(x)
print(y)

# Using reshape
b = np.arange(10).reshape(2,5)
print(b)
c = np.arange(24).reshape(2,3,4)  
print()
print(c)

#Basic operators
a = np.array([1, 2, 3, 4])
b = np.arange(4)
print(a-b)
print(b**2)
print(np.sin(a))

a = np.array(([1, 2], [3, 4]))
b = np.array(([1, 2], [3, 4]))
print(a * b)  # Element-wise product
print(a @ b)  # Matrix multiplication
print(np.dot(a, b)) # dot product multiplication
print(a.dot(b)) #dot product