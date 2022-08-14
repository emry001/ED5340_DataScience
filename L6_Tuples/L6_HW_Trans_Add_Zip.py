#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:28:04 2021

@author: ramanathanmuthuganapathy
"""


mat = [[1,2,3], [4,5,6]]
for ite in zip(mat[0], mat[1]):
    print('Each tuple in zip = ', ite, 'sum of the each tuple = ', sum(ite))
    print('Priting the elements of each tuple using index ', ite[0], ite[1])
    print('same result as above but using unpacking', *ite)

print(mat[0], mat[1]) 
print(*mat)
for it in zip(*mat):
    print(sum(it))
    
#Matrix inverse
ite = zip(*mat)
lst = list(ite)
print('Matrix inverse = ', lst)


mat1 = [[20,30,40], [50,60,70]]
print(mat1)
ite = zip(mat, mat1)
print(*ite)
mat2 = [[sum(a) for a in zip(*b)] for b in zip(mat, mat1)]
print(mat2)
