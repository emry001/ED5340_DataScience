#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:31:40 2020

@author: ramanathanmuthuganapathy
"""


#To demonstrate tuple varieties

#Creating tuple of tuples

tup1 = (1, 2, 3, 4)
tup2 = (6, 7, 8, 9)
tup_tup = (tup1, tup2)

print('combining to tuples : ', tup_tup)

#You can also create directly

tup_tup = (('Ram', 25, 45.5),
           ('Raman', 28, 32.45))

print('directly defining the 2D tuple : ', tup_tup)

#Similar to list, 2D array index can be used to access 2D tuple

print('Array index usage ', tup_tup[0][1], tup_tup[1][0], tup_tup[1][2])

print('Printing each row : ', tup_tup[0], tup_tup[1])

print('Printing individual elements in each row using unpakcing operator', *tup_tup[0], *tup_tup[1])

#Similar to the list, you can do the following, but not as comprehension
print('Printing each element using two for loops')
for ele in tup_tup:
    for each in ele:
        print(each)

print('Using comprehension')
[print(each) for ele in tup_tup for each in ele]
#tuple embedding

tup1 = ('Ram', 25)
tup2 = ('Raman', tup1)

print('Tuple embdedding : ', tup2, tup2[1])

#Tuple unpacking using * operator

tup3 = ('Ramanathan', *tup1)

print('Tuple unpacking : ', tup3)

#
# This is a generator - we will see that later in more detail
#gen = []        
#gen = (each for ele in tup_tup for each in ele)
#print('unpacking gen ',*gen, type(gen))
#