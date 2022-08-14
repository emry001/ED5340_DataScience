#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 20:02:48 2021

@author: ramanathanmuthuganapathy
"""


import numpy as np

print(np.__version__)

print('Numpy stands for numerical python')

#1D Array
arr = np.array([1, 2, 3, 4, 5]) # 

print(id(arr), id(arr[0]))
print(arr.itemsize, arr.strides) #Here the itemsize is a 8 bits (size of one integer). 
print(type(arr))
for i in range(0, len(arr)):
    print(i, arr[i], id(arr[i])) #We can't print the id of each index of arr unlike in C. 
    
arr1 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

print(id(arr1), id(arr1[0]))
print(arr1.itemsize, arr1.strides) #itemsize is 40 (8*5) and stride is (40,8)
for i in range(0, len(arr1)):
    print(i, arr1[i], id(arr1[i]))

print(arr1)

arr2 = np.array((1, 2, 3, 4, 5))#You can pass a tuple or a list

print(arr2, type(arr2))