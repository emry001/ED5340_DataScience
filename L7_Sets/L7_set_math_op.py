#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:40:16 2020

@author: ramanathanmuthuganapathy
"""


setA = {10, 20, 30, 40, 40, 50}
setB = {30, 40, 50, 60, 70}

print('Union of two sets : ', setA | setB)
print('Intersection of two sets : ', setA & setB)
print('A - B : ', setA - setB)
print('B - A : ', setB - setA)
print('Symmetry difference of two sets : ', setA ^ setB)

setC = setA - setB
setD = setB - setA
print('Symmetry difference of two sets : ', setC | setD)

setA -= setB
print(setA)