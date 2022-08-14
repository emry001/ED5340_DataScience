#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 00:38:20 2021

@author: ramanathanmuthuganapathy
"""


#Generator and generator expressions

#Returns the data everytime using the yield
def IterData(data):
    for i in range(0, len(data)):
        print(i)
        yield data[i]

lst = [10, 20, 30, 40, 50]
for i in IterData(lst):
    print(i)        

#Returns the average 
def AvgData(data):
    for i in range(0, len(data)-1):
        yield (data[i] + data[i+1])/2
        
lst = [10, 20, 30, 40, 50]
for i in AvgData(lst):
    print(i)
    
#generator expression
import random
print(max(random.randint(0,100) for n in range(20)))

print(sum(n * n for n in range(10)))

#memory savings!

import sys
lst = [i * i for i in range(15)]
gen = (i * i for i in range(15))
print('printing the memory details')
print(sys.getsizeof(lst))
print(sys.getsizeof(gen))