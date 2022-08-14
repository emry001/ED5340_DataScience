#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:52:54 2020

@author: ramanathanmuthuganapathy
"""

# To demonstrate the use of import

import math

y = math.pi
print('Fetched the value of pi using math.pi', y)
x = y/3 
print('using the cos function available in math library',math.cos(x))

from math import cos
print('using the cos function available in math library',cos(x))

help(math)
help(cos)