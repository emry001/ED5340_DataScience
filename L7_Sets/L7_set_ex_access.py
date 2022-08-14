#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:01:25 2020

@author: ramanathanmuthuganapathy
"""


#Set example and access

empty_setA = ()  #This is an empty tuple
print(type(empty_setA))

empty_setB = {} #This is an empty dictionary
print(type(empty_setB))

print('\n')
print('Neither of them gave an empty set. What to do?')
empty_setC = set() # Need to call the 'set' function

print('Note the above notation of empyt set: ', type(empty_setC))

print(empty_setC)

if not empty_setC:
    print('Empty set')
    
setA = {10, 20, 30, 40, 50}

print('setA = ', setA) # What do you observe

print('Printing using iterator and for loop')
for it in setA:
    print(it)

setB = {25, 45.4, 'Ram', 35.5, 'Shyam'}
print('setB = ', setB) 

setC = {100, 100, 100, 100}
print('setC = ', setC) 
