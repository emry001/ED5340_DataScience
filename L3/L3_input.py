#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:07:15 2020

@author: ramanathanmuthuganapathy
"""

#Demonstrating the console input and ouput

a = input('Enter first value: ')
b = input('Enter second value: ')

print('Object types of a and b are ', type(a), type(b))

c = a+b
print(c) #Why is this answer?

print('Object type of c is ',type(c))

#a and b need to be converted to int
c = int(a) + int(b)

print(c) 

print('Object type of c is ',type(c))

#Input multiple values using input() and split() functions
a, b = input('Enter input values a and b: ').split()

c = int(a) + int(b)

print(c) 

#Enter multiple data type input
n, a, s = input('Enter name, age, salary: ').split()
a = int(a)
s = float(s)
print('Printing name, age, salary: ',n, a, s)

data = input('Enter name, age, salary with comma: ').split(',')
name = data[0]
age = int(data[1])
salary = float(data[2])
print('Printing name, age, salary: ',name, age, salary)