#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:08:17 2020

@author: ramanathanmuthuganapathy
"""


#To demonstrate the default output and formatted output 

#Standard print
a, b, c = 1, 2, 3

print('Default print with sep as space and end as newline', a, b, c)

print('a = ', a, ',', 'b = ,', b, 'c = ,', c)
print(a, b, c, sep = '+') #separator as + and end as newline

#separtor as + and end as tab space
print(a, b, c, sep = '+', end = '\t')
print(a, b, c, sep = '+', end = '!')
print('\n')

#Using formatted string literals
print(f'a = {a}, b = {b}, c = {c}')

#Using format() -- print in order
print('a = {}, b = {}, c = {}'.format(a, b, c))

