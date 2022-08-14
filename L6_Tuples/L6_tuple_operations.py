#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:05:49 2020

@author: ramanathanmuthuganapathy
"""


#Operatiion in tuples

#Tuples are IMMUTABLE

tup1 = ('Ram', 24, 55.6)

print(tup1)

tup1 = ('Ram', 24, 55.6, 'Shyam')

print(tup1)

# tup1[0] = 'Sam' - Not possible to do this, similar to a list

#Tuples can contain mutable objects like list.

tup2 = ([10,20], 'Ram', 44.3)

print('tuple containing mutable objects',tup2)

#tup2[0] = [20, 10]

#Containment check
print('Ram' in tup1)

print('CW: WAP to do the following operations on a tuple - len, str to tuple, max, min, sum, sorted')

# print('Anything different that you observed?')

print(sum(tup2[0]))

# print(sorted(tup1))

#Tuple concatenation

tup3 =  tup1 + tup2

print('concated tuple is : ',tup3, id(tup3))

tup3 += tup1

print('Tuple is immutable, but why that worked?')
print('concated tuple is : ',tup3, id(tup3))

#Reversing a tuple

tup4 = reversed(tup1)
print('Reversed tuple', tuple(tup4))

#Comparison of tuples
#print(tup1 <= tup1)

print('HW - Find out instances where comparison will give error')

#tup1[1:3] = ()

tup_comp = tuple([(x**2, x**3) for x in range(5)])
print('Tuple from a list comprehension : ', tup_comp)

for i in tup_comp:
    print(i)


#tup5 = tup1[::-1]
#print('Reversing a tuple using indexing method :', tup5)