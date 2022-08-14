#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:48:04 2020

@author: ramanathanmuthuganapathy
"""
import sys
#integers
a = 23
print('a = ', a, ' , ', 'sizeof(a) = ', sys.getsizeof(a) )
print('object type of a is ', type(a))

#arbitray precision
b = 10000000000000000000
print('b = ', b, ' , ', 'sizeof(b) = ', sys.getsizeof(b) )
print('object type of b is ', type(b))

#float
c = 2.35
print('c = ', c, ' , ', 'sizeof(c) = ', sys.getsizeof(c) )
print('object type of c is ', type(c))

#complex
d = 3+4j
print('d = ', d, ' , ', 'sizeof(d) = ', sys.getsizeof(d) )
print('object type of d is ', type(d))

#bool
e = 5; g = 6;
h = e < g
print('h = ', h, ' , ', 'sizeof(h) = ', sys.getsizeof(h) )
print('object type of h is ', type(h))

#strings
str = "Ramanathan"
print('str = ', str, ' , ', 'sizeof(str) = ', sys.getsizeof(str) )
print('object type of str is ', type(str))

#No chars
str1 = 'R'
print('str1 = ', str1, ' , ', 'sizeof(str1) = ', sys.getsizeof(str1) )
print('object type of str is ', type(str1))

