#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:37:51 2020

@author: ramanathanmuthuganapathy
"""


#To demonstrate string accessing and slicing

str = 'Raman'

print(str[0])
print(str[-1])
print(str[-0])
print(str[4])

#string slicing

print(str[0:4])

print(str[0:2])

#When using negative indices, you have to be careful
#Tell the answer for the following
print('printing from -5 to -1: ', str[-5:-1])
print('printing from -1 to -5: ', str[-1:-5]) #This will not produce any result
#My hypothesis - 'end' index should be greater than 'start' index
print(str[0]+1) #Not a pointer, this will not work