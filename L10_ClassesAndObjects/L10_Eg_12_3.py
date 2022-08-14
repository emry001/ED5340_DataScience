#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:08:38 2020

@author: raman
"""


#Problem 12.3

#Program that displays the attibuts of integer, float etc..

def fun():
    print('Everthing is an object')
    
print(dir(55))
print(dir(-5.67))
print(dir(fun))
print((5).__add__(6))
print((-5.85).__abs__())
d = globals()
d['fun'].__call__()
