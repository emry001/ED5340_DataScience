#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:47:01 2020

@author: ramanathanmuthuganapathy
"""

#Strings are immutable

str = 'Kite'

print(str)

#str[0] = 'L' # You cannot do this in Python

print(str)

print('string is immutable, i.e, you cannot change the characters')

# # Let us dwell into little bit more detail
# print(id(str), id(str[0]))
# print('They are not same as in C')

# print('mem id of each individual elements')
# for i in range(len(str)):
#     print(id(str[i]))

str = 'Ramanathan'
print(str)

# print(id(str), id(str[0]))
# print('mem id of each individual elements')

# for i in range(len(str)):
#     print(id(str[i]))

# print('str[0] = L implies that you are creating another object of str[0], which is not possible')

#Are integers mutable or immutable?
a = 5
print(id(a))
a = 10
print(id(a))
b = 10
print(id(b))

