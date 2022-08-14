#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:07:15 2020

@author: ramanathanmuthuganapathy
"""


# List contatiner - few examples

lst1 = [10, 200, 300, 40]

lst2 = ['cow', 'bull', 'tiger', 'lion', 'rhinoceros', 'antelope']

lst3 = [12.5, 6.5, 7.45, 6.456, 6.5, 2.34, 5.78, 8.95, 1.2345]

#Mixed datatype list
lst4 =  [12, 45.4, 'Raman']

#Empty list using square brackets
lst5 = []

#Printing a full list - just give the name of the list

print(type(lst1),lst1)

print(lst2)

print(lst3)

print(lst4)

print(lst5)

#List is Iterable. You can iterate over the list

print('Printing the elements of lst1')
for i in lst1:
    print(i)
    
print('Printing the elements of lst2')
for i in lst2:
    print(i)

print('Printing the elements of lst3')
for i in lst3:
    print(i)
    
print('Printing the elements of lst4')
for i in lst4:
    print(i)
    
print('Printing the elements of lst5')
for i in lst5:
    print(i)

#Print a portion of a list - slicing
print('Printing a portion of a list - slicing')
print(lst1[1:3])
print(lst1[1:])

#Memory ids of list elements
# print('Printing memory ids of a list')
# for i in range(len(lst1)):
#     print(id(lst1[i]))
    
lst6 = [lst1, lst2, lst3, lst4]
print(type(lst6), lst6)

