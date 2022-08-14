#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:14:41 2020

@author: ramanathanmuthuganapathy
"""


#str1ing functions
#Contest test functions
str1 = "Ramanathan Ram"
print(str1.isalpha()) # True if every character is an alphabet
print(str1.isdigit()) 
print(str1.isalnum()) #True if each char is either alphabet or a digit
print(str1.islower()) #True if every character is lower case
print(str1.isupper())
print(str1.startswith('R'))
print(str1.endswith('n'))

#Conversion functions
str1 = " you are learning python now"
print(str1.upper())
print(str1.lower())
print(str1.capitalize()) #Makes the first letter to be capital
print(str1.swapcase())

#Search and find functions
print(str1.find('a'))
print(str1.replace('a', 'b', 1)) #Does not change str1, only prints
print(str1)

print(str1.split()) #Splits the str1ing at blank spaces
print('split() is a very important string function')
print(str1)
print(str1.split('a')) #Splits the str1ing at character a
print('split() is a very important string function')
print(str1.lstrip('y'))
print(str1.partition('a'))
print(str1.index('are'))

age = 25
print('she is '+ str(age))
print('counting the num of a\'s:', str1.count('a'))
print('Find out other functions: len(), rstr1ip(), partition(), str1(), chr(), ord(), index() etc.')

