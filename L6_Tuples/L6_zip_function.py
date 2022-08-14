#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:58:55 2020

@author: ramanathanmuthuganapathy
"""

#zip() function - a very important one

#Takes one or more iterables and groups them together

#returns an iterator of tuples

names = ('Ram', 'Raja', 'Geetha', 'Ramya')
gender = ('male', 'male', 'female', 'female')

print('printing 1st tuple')
for n in names:
    print(n)
print('\n')
print('printing 2nd tuple')
for g in gender:
    print(g)

print('\n')
print('Grouping using code and not through zip')    

lst = []

for index in range(len(names)):
    lst.append((names[index], gender[index]))

print('printing as list')
print(lst)
    
tup = tuple(lst)

print(tup)

tup = [(names[index], gender[index]) for index in range(len(names))]
tup1 = tuple(tup)

print(type(tup), '\n', tup, tup1)
print('\n')
#Both gender and names are iterables. The job of combining the two iterables can be done by using zip() function.

ite1 = zip(names,gender)

print('Type of ite', type(ite1))

print('\n')
#needed to unpack to print the tuple
print('Unpacked the returned tuple from zip',*ite1)

#You can iterate 'ite' using the for loop as follows
print('\n')

print('Printing using unpacking iterator in for loop')
for ite in zip(names, gender):
    print(*ite, ite)
print('\n')

print('Printing using iterator index')
for ite in zip(names, gender):
    print(ite[0], ite[1])
print('\n')
 
print('Via. for loop itself - for loop does magic!')
for (n,g) in zip(names, gender):
    print(n, g, '\t', *n, *g)
    
#printing the type of n and g
print('\n')
print('type(n) = ', type(n), 'type(g) = ', type(g) )

print('\n')
#You can convert the zipped one into a list   
ite = zip(names,gender)
lst = list(ite)
#new_tup = tuple(*ite) #This won't work

print('list from iterator \n', lst)
print('In fact, it is a list of tuples!', type(lst), type(lst[0]))

#You can uznip this lst using zip operator again!
print('\n')
print('uznip this lst using zip operator again!')
(n1,g1) = zip(*lst)
print(n1)
print(g1)

#printing the type of n1 and g1
print('\n')
print('type(n1) = ', type(n1), 'type(g1) = ', type(g1) )