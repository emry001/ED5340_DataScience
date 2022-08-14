#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:52:51 2021

@author: ramanathanmuthuganapathy
"""


class Complex:
    def __init__(self, r=0, im=0):
        self._real = r
        self._imag = im
        print(self)
        
    #Addition of two complex numbers using a method
    def add_comp(self, other):
        c = Complex()
        c._real = self._real + other._real
        c._imag = self._imag + other._imag
        return c
    
    #Addition of two complex numbers using operator overloading
    def __add__(self, other):
        c = Complex()
        c._real = self._real + other._real
        c._imag = self._imag + other._imag
        return c
    
    def print_comp(self):
        print('real = ', self._real, 'imag = ', self._imag)
    
f = open('ComplexData.txt', 'w+') #Reading and writing
f.write(str(12.3))
f.write('\n')
f.write(str(4.56))
f.seek(0)
a = float(f.readline())
b = float(f.readline())
c = a + 2.5
d = b + 4.32
c1 = Complex(a, b)
c2 = Complex(c, d)
#c3 = Complex()
#c3.print_comp()
c3 = c1.add_comp(c2)
c1.print_comp()
c2.print_comp()
c3.print_comp()

c3 = c1 + c2  #Using the symbol for addition
c3.print_comp()
f.close()