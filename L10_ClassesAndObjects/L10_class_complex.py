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
    
c1 = Complex(4.5, 5.45)
c2 = Complex(3.5, 8.45)
#c3 = Complex()
#c3.print_comp()
c3 = c1.add_comp(c2)
c1.print_comp()
c2.print_comp()
c3.print_comp()

c3 = c1 + c2  #Using the symbol for addition
c3.print_comp()
