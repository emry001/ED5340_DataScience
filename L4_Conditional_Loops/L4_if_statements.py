#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:45:38 2020

@author: ramanathanmuthuganapathy
"""


# To demonstrate basic if - elif - else

a, b = input('Enter two values a and b: ').split()
a = int(a)
b = int(b)

#print(a is b)

if a<b:
    print('a less than b')
else:
    print('a greater than or equal to b')
    
#Discount  
    
item = input('Enter the value for number of items : ')
item = int(item)
if item < 10:
    dis = 100
elif item < 20:
    dis = 200
else:
    dis = 500
    
print(f'num. of items = {item}, dis = {dis}')

a, b, c, d = 1, -2, -3, 4
print(a == b)

if a < b:
    if a < c:
        print('a is the smallest')
    else:
        print('c is the smallest')
else:
    if b < c:
        print('b is the smallest')
    else:
        print('c is the smallest')
    

if a < b < c:
    print('a is the smallest')
elif b < c < a:
    print('b is the smallest')
else:
    print('c is the smallest')


if a < b < c < d or d > c > b > a:
    print('True')
    
#Conditional expression
maxi = a if a > b else b
print('max value of a and b using conditional expression is ', maxi)

