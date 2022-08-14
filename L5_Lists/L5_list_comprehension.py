#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:07:23 2020

@author: ramanathanmuthuganapathy
"""


#To illustrate List Comprehension

lst = [num for num in range(10)]

print('List created using list comprehension', lst)

#The above is equivalent to the following

lst = []
for num in range(10):
    lst.append(num)

print('List created using append()', lst)

import random

lst1 = [random.randint(10, 100) for n in range(15)]

print(lst1)

print('CW: Write the equivalent code using append()')

lst2 = [[x, x**2, x**3] for x in range(10)]

print('list of lists with squares and cubes:',lst2, type(lst2))

#Use if condition in comprehension

lst3 = [x for x in range(20) if x%2 == 0]

print('list of even numbers', lst3)

print('CW: Write the equivalent code using append()')

lst4 = [x for x in range(20) if x%2 == 0 ]

print('list of even numbers less than 10', lst4)

lst4 = [x for x in range(20) if x%2 == 0 if x > 10 and x < 15]

print('list of even numbers less than 10 and also another if', lst4)

print('CW: Generate a list of odd numbers. Delete the numbers from the list that is not divisible by 3')

#Console input made into a list
lst5 = [int(num) for num in input('Enter the numbers : ').split()]
print('Entered numbers from the keyboard: ', lst5)

#if-else
al_list = []
for alph in 'alphabet':
    if alph in 'aeiou':
        al_list.append(alph)
    else:
        al_list.append('!')
        
print(al_list)

#Using list comprehension
al_list1 = ['!' if alph not in 'aeiou' else alph for alph in 'alphabet']
    
print(al_list1)

