#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:11:02 2021

@author: raman
"""


#map(function, listofinputs)
#map applies the function to each element in the list

lst1 = [1, 2, 3, 4, 5]

lst2 = map(lambda x : x ** 2, lst1)

print(type(lst2))

#should be converted to a list using list()
lst3 = list(lst2)

print(lst3)

# Take the two lists and add each of them

lst4 = map(lambda x1,x2 : x1+x2, lst1, lst3)

print(list(lst4))

#We can also define a function and pass it instead of lambda
def squ(x):
    return x*x

lst5 = map(squ, lst1)

print(list(lst5))

#filter - filters the elements in a sequence acc to a condition
def gre(x):
    if x > 10:
        return x
    else:
        return x-5

    
lst6 = filter(gre, lst3)

print('output = ' , list(lst6))

lst6 = filter(lambda x : x if x > 10 else x-5, lst3)

print('output = ' , list(lst6))

#reduce - rolling computation to sequential pairs of elements
#in a sequence

from functools import reduce

lst7 =  reduce(lambda x,y : x+y, lst1)

print(lst7)

lst8 =  reduce(lambda x,y : x*y, lst1)

print(lst8)


