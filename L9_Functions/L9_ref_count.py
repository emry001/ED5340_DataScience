#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:55:31 2020

@author: ramanathanmuthuganapathy
"""


import sys, gc
import ctypes
x11 = 5
my = 5
stri = 'Vidushi'
print(sys.getrefcount(stri))
#print(len(gc.get_referrers(x1)))



my_var = 'hello python'
my_var_address = id(my_var)

id1 = id(my)

print(ctypes.c_long.from_address(id1).value)

print(ctypes.c_long.from_address(my_var_address).value)

