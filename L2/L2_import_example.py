#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:11:20 2020

@author: ramanathanmuthuganapathy
"""


# To demonstate using a module - math
#help(round)
import math

r = 5
area = math.pi * r ** 2
print(area)

a = math.cos(math.pi / 3) # Need to use math.cos and math.pi

print(a)
# You can import single function from a module

from math import cos
from math import pi

a = cos(pi / 3) # cos and pi can be used directly

#rounding using round function
print(round(a, 3))


#help(math)
#help(cos)

# To know the functions in the module, you need to know the 
# existence of the module.
#import cmath
#help(cmath)