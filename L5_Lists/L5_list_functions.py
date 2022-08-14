#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 17:13:51 2020

@author: ramanathanmuthuganapathy
"""


#Member functions for a list

lst = [10, 30, 20, 15, 20, 60, 80, 70]

print('Printing the list', lst)

lst.append(23)

print('Printing the list after appending', lst)

lst.pop()

print('Printing the list after pop()', lst)

lst.pop(3)

print('Printing the list after popping 4th element', lst)

lst.sort()

print('Printing the list after sorting', lst)

lst.remove(20)

lst.insert(3, 34)   

print('Printing the list after insertion', lst)

print('number of occurances of 20: ',lst.count(20))

print('index of number 20: ', lst.index(10))

lst.sort(reverse=True)

print('Printing the list after sorting', lst)

lst.reverse()

print('Printing the list after sorting in reverse', lst)

help(list())