#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 15:18:31 2020

@author: ramanathanmuthuganapathy
"""


#To demonstrate the list copying 
#Shallow copy

lst1 = [1, 2, 3, 4, 5]
lst2 = lst1

print(lst1, lst2)

#Change one of the elements in lst2
lst2[0] = 100

print(lst1, lst2)

#What did you observe and why that happened?

print('Memory ids of the lists in shallow copying, ',id(lst1), id(lst2))

#Deep copy - Make the lists different

lst2 = [] #Create an empyt list

lst2 += lst1

print('lists after deep copy: ', lst1, lst2)

lst2[0] = 555

print('lists after deep copy but changing lst2[0] : ', lst1, lst2)#Only lst2[0] has got changed, which is understandble. 

print('Memory ids of the lists in deep copy, ',id(lst1), id(lst2))

#What happens in deletion
lst3 = lst2 = lst1
#lst1 = lst2 = lst3
print('After multiple assignment: ',lst1, lst2, lst3)

print('Memory ids of the lists, ',id(lst1), id(lst2), id(lst3))

#Suppose make the 1st list empty
lst1 = []

#What will be the answer to the following
print('After multiple assignment, making lst1 as empty: ', lst1, lst2, lst3)

print('After multiple assignment, making lst1 as empty, memory ids: ', id(lst1), id(lst2), id(lst3))

lst1 = lst2 = lst3

#What will be the answer to the following
print(lst1, lst2, lst3)

lst2[:] = [] #What does this indicate
#What will be the answer to the following
print(lst1, lst2, lst3)

#Comparing lists

lst4 = [1, 2, 3, 4, 5]
lst5 = [1, 2, 3, 4, 5]
print('mem. ids of 4 and 5: ', id(lst4), id(lst5))
print('Note that even though both lists contains the same elements, they are not same lists')
lst6 = [5, 2, 3, 4, 1, 6]

print(lst4 is lst5) # 'is' test, not an 'in' test: checks whether the lists are same objects (ids)
print(lst4 is lst6)
print(lst5 is not lst6)

#You can also use 'in' test

print(1 in lst4)
print(2 in lst4)
print(10 in lst5)

#No sublist matching!
print([1, 2] in lst4)

print(lst4 == lst5)

lst7 = ['Rama', 'Calm', 'Shyam']
lst8 = ['Ram', 'Came', 'Shyam']
print(lst7 < lst8)
print(lst4 < lst7)