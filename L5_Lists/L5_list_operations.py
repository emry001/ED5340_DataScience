#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:40:48 2020

@author: ramanathanmuthuganapathy
"""

#List operations - though built-in functions
#List is MUTABLE

lst = [10, 20, 30, 40, 50]
print(lst)
lst[0] = 100
print('muted list', lst)
lst[2:5] = [300, 400, 500]
print('muted list', lst)

#different way of deleting
lst[:] = []
print('deleting using empty list symbol', lst)

#Lists concatenation
lst1 = [6, 7, 8, 9]
lst += lst1
print('concatenated lists:', lst)

#searching (containment) and sorting - in and not in functions
print('a' in ['a', 'e', 'i'])
print('b' in ['a', 'e', 'i'])

vow_lst = ['o', 'a', 'e', 'i']
vow_s_lst = sorted(vow_lst) # does not change the original list

print('original list is ', vow_lst, ',', 'sorted list is ',vow_s_lst)
print(type(vow_s_lst))

#Deleting using del function
del(vow_lst[2])
print('List after deleting index 2 element is :',vow_lst)
del(vow_lst[:])
print('List after deleting all elements is :',vow_lst)

#Conversion
#String to list
print(list('Raman')) #prints a list of characters
#What will be answers to the following 
print(max(list('Raman')))
print(min(list('Raman')))
print(sorted(list('Raman')))
print(len(list('Raman')))

#checking if the list is empty or not
lst = []
if not lst:
    print('True')
    
print('CW: Define a list of marks for a student and find the max, min and average of them. Arranged the in sorted order. Print all of them clearly')

lst1 = [6,7,8,9]
max1 = max(lst1)
print(max1)
lst1[2:3] = []
print(lst1[2])
print(lst1)
del(lst1[2])
print(lst1)
