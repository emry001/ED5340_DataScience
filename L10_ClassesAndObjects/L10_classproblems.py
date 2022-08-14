#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:44:51 2020

@author: raman
"""


#Problems in this chapter - 12.1
class Fruit:
    count = 0
    def __init__(self, name = 'R', size = 0, color = 'Y'):
        self.name = name
        self.size = size
        self.color = color
        Fruit.count += 1
    
    def display():
        print(Fruit.count)
        
f1 = Fruit()
f1 = Fruit('Orange', 23, 'Orange')
f2 = Fruit('Mosambi',43, 'Yellow')
f3 = Fruit('Grape', 44, 'Green')

Fruit.display()

#Without operator overloading
class Complex:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
    
    def plusop(self, C1, C2):
        self.real = C1.real + C2.real
        self.imag = C1.imag + C2.imag
        
    def minusop(self, C1, C2):
        self.real = C1.real - C2.real
        self.imag = C1.imag - C2.imag
        
C1 = Complex(2.5, 5.5)
C2 = Complex(3.5, 6.5)
C3 = Complex(0,0)
C3.plusop(C1,C2)
print(C3.real, C3.imag)
C4 = Complex()
C4.minusop(C1,C2) 
print(C4.real, C4.imag)    

if C3 is C4:
    print('C3 and C4 points to the same object')
else:
    print('C3 and C4 points to a different object')
    
if type(C3) == type(C4):
    print('C3 and C4 points to the same type')
else:
    print('C3 and C4 points to a different type')
        