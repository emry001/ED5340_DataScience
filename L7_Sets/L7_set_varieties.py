#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:40:24 2020

@author: ramanathanmuthuganapathy
"""

#Set varieties
#Set of sets

# setofsets = {{10, 20, 30},
#        {40, 50, 60}}

setA = frozenset({10, 20, 30})
setB = frozenset({40, 50, 60})
fr_sos = {setA, setB}

print('using frozen sets',fr_sos)
# setA.add(34) #You can't add in a frozen set
#Making a set of sets via tuples which are immutable
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)

setC = set()
setC.add(tup1)
print(setC)
setC.add(tup2)
print('set of sets using tuples - set of tuples',setC)

setA1 = {1, 2, 3}
# setB1 = {4, 5, setA1} # Error - Set embedding not allowed

setC1 = {4, 5, *setA1} #unpacking operator
print('set using unpacking operator * ', setC1)

