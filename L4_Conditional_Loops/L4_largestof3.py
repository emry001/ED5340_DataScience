#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 12:08:50 2021

@author: raman2020
"""

a= 500
b = 20000
c = 10

#Using relational
if a<b<c:
    print('a is the smallest')
elif b<c:
    print(' b is the smallest ')
else:
    print('c is the smallest')
    
#Using relational
if a<b<c:
    print('a is the smallest')
elif a<b:
    print(' a is the smallest ')
elif b<c:
    print(' b is the smallest ')
else:
    print('c is the smallest')
    
#using relational and logical
if a<b and a<c:
    print('a is the smallest')
elif b<c:
    print(' b is the smallest ')
else:
    print('c is the smallest')
    
if a < b:
    if a < c:
        print('a is the smallest')
    else:
        print('c is the smallest')
else:
    print('b is the smallest')





#Using conditional expression

maxi = a if a > b else b

#maxi1 = maxi  if maxi > c else c

#print(maxi, maxi1)
