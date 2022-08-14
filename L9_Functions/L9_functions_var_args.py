#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:22:52 2020

@author: ramanathanmuthuganapathy
"""


#Variable length positional arguments

def var_arg(*args):
    #su = 0
    for var in args:
        #su += var
        #print(su, var)
        print(var, type(var))
        
var_arg('passing two arguments', 1, 5)
var_arg('passing three arguments', 1, 5, 'Ram')

lst = [1,2,3]
var_arg(lst)

#Variable length keyword arguments

def kwvar_arg(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
        
kwvar_arg(i = 10)
kwvar_arg(i = 10, j = 20.34)
kwvar_arg(i = 10, j = 20.34, k = 'Ram')

# lst = [1,2,3]
# kwvar_arg(*lst)

# dc = {'Ram' : 24, 'Rama' : 35}

# kwvar_arg(**dc)

#default argument

def TorF(cond = True):
    if cond == True:
        print('True')
    else:
        print('False')
        
TorF()
TorF(False)