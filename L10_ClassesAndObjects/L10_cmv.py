#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:48:13 2021

@author: ramanathanmuthuganapathy
"""

#To demnostrate class variables and methods
import math

class CMV:
    count = 0
    
    def __init__(self, n = '', s = 0, c = ''):
        self._name = n
        self._size = s
        self._color = c
        CMV.count += 1
    
    def display():
        print(CMV.count)
        
c1 = CMV('R', 1, 'B')
print(CMV.count) 
c2 = CMV('R', 1, 'B')
print(CMV.count) 
CMV.display()

# print(vars(CMV))  #dictionary of attributes
# print()
# print(dir(CMV))   #list of attributes

# print(vars(math))
# print()
# print(dir(math))