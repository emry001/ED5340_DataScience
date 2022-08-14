#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 11:59:36 2020

@author: ramanathanmuthuganapathy
"""


#To demonstrate dictionary comprehension

namelist = {'name1' : 'Anand', 'name2' : 'Ramesh', 'name3' : 'Kamesh'}
dctA = {k:v for(k, v) in namelist.items()}

print(dctA)

dctB = {10 : 10, 20 : 23, 30 : 46, 40 : 49, 50 : 57}


print('\n')
print('CW: Using comprehension, from dctB, make a dictionary containing only even numbers as its values')

dctC = {i:i**2 for i in range(5)}

print(dctC)

print('\n')
print('HW: Suppose there are two lists. Assume one of them to contain the keys and the other, values. Use comprehension to make a dictionary out of the two lists')