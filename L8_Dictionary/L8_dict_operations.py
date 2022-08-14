#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 08:51:29 2020

@author: ramanathanmuthuganapathy
"""


#To demonstrate some dictionary operations

courselist = {'ED2' : 'Intro to Comp', 'ED1' : 'Python', 'ED4' : 'DSA', 'ED3' : 'Geometric Modeling'}

#Add, modify and delete courses
print('full list of courses : ', courselist)
courselist['ED5'] = 'Computational Geometry'
print('\n')
print('course list after addition : ', courselist)

courselist['ED2'] = 'ChangedCourse'
print('course list after changing : ', courselist)

del(courselist['ED1'])
print('\n')
print('course list after deletion : ', courselist)

# del(courselist) #This will delete the object, you cannot print after that
# print('\n')
# print('course list after deleting all : ', courselist)

#You cannot change the size of the dictionary during runtime
# for k in courselist.keys():
#     del(courselist[k])

#Using list
lst = list(courselist.keys())
print('Printing the keys using list',lst)

lst = list(courselist.values())
print('Printing the values using list',lst)

lst = sorted(list(courselist.items()))
print('Printing the key-value pairs using list',lst)