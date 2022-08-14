#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 23:38:32 2020

@author: ramanathanmuthuganapathy
"""
#On list of lists - 2D array

arr = [[1,2,3,4], [5,6,7,8]]
print('What will be the answer to the following?')
print('arr = ', arr, '*arr = ', *arr)
print('What are your observations?')

print('What will be the answer to the following?')
print('arr[0] = ', arr[0], 'arr[1] = ', arr[1])
print('*arr[0] = ', *arr[0], '*arr[1] = ', *arr[1])
print('What are your observations?')

#To get the number of rows and columns
print('number of rows = ', len(arr))
print('number of columns = ',len(arr[0]))

arr_lst = []
for ele in arr:
    print('elements of each row', ele)
    for num in ele:
        arr_lst.append(num)
        
print(arr_lst)

arr_lst1 = [num for ele in arr for num in ele]
print(arr_lst1)

print('CW: Convert the arr_list to a list comprehension')

print('How does the output look after list comprehension?')

#Nested for loops in comprehension
lst6 = [a+b for a in [1,2,3] for b in [4,5,6]]

print('single flattened list', lst6)

#Using nested comprehension - list of lists

lst7 = [[a+b for a in [1,2,3]] for b in [4,5,6]]

print('produces list of lists', lst7)

print('CW - Given two row matrices A and B, print the added matrix C')
print('CW: Unpack the arr into one single list (a) using list comprehension and (b) without list comprehension')

print('HW - Generate all unique combinations of 1, 2 and 3 using list comprehension')

print('HW - Define two matrices of 3X5 and add them. Print all the matrices in row and column form')