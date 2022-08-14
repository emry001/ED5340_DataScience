#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:18:41 2020

@author: ramanathanmuthuganapathy
"""


#Tuple representation and accessing

empty_tup = ()
one_tup = (1100,)
mix_tup = ('Ram', 25, 45.55)

#While initialization, you can drop the brackets
tup1 = 'Ram1', 2345, 234.5556

print(type(tup1))

# Tuple can be sliced
print(tup1[1:3])

#Other ways of creating tuples from strings, lists etc. using the keyword 'tuple'

tup_str = tuple('Ramanathan')
print('Tuple from a string : ', tup_str)

tup_lst = tuple([10.5, 24.5, 22.4])
print('Tuple from a list : ', tup_lst)

#Accessing the tuples - similar to list

print('printing the elements of a tuple: ',mix_tup[0], mix_tup[1])
print('printing the elements of a tuple: ',mix_tup[0:2]) #Index value

print('Full tuple using its name: ', tup1)

#del(tup1[0]) - No del function

#print('Full tuple using its name: ', tup1)

#Accessing using iterator

for each in tup1:
    print('each element using iterator : ', each)

#Note that this is a tuple of tuples!
    
stud_details = (('stud1', 55, 6.7),
                ('stud2', 65, 7.6),
                ('stud3', 75, 8.7),
                ('stud4', 85, 7.7))

#Printing like columns
for n, m, c in stud_details:
    print(n, m, c)
    
print(*stud_details[0])

#help(tuple)



