#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:43:03 2021

@author: ramanathanmuthuganapathy
"""

a = 100000
b = 7000
c = 780
maxi = a if a > b else b

maxi1 = maxi  if maxi > c else c

print(maxi, maxi1)

maxi2 = a if a > b > c else b if b > c else c

print("maxi2 = ", maxi2)

0

#a = not a

#a != b != a 
print(a == b == a )

