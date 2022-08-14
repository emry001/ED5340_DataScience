#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 00:16:43 2021

@author: ramanathanmuthuganapathy
"""


#To demonstrate Multiple inheritance

class Base1:
    def __init__(self, name):
        self.name = name
        print('Inside base1 constructor')
          
    def printbase1(self):
        print('Inside base1 print')
        print(self.name)
        
    def printdata(self):
        print('Inside base1 printdata')
        print(self.name)

    
class Base2:
    def __init__(self, roll):
        self.roll = roll
        print('Inside base2 constructor')
          
    def printbase2(self):
        print('Inside base2 print')
        print(self.roll)
        
    def printdata(self):
        print('Inside base2 printdata')
        print(self.roll)


class Derived(Base1, Base2):
    def __init__(self, name, roll):
        #super().__init__(name)
        Base1.__init__(self, name)
        Base2.__init__(self, roll)
        print('Inside derived1 constructor')
    
    def printderived1(self):
        print('Inside derived1 print')
        print(self.name, self.roll)
        
    def printdata(self):
        #super().printdata() #Access Base1 printdata
        print('Inside derived printdata')
        print(self.name, self.roll)

d1 = Derived('Ram', 12345)
d1.printderived1()
d1.printbase2()
d1.printbase1()
d1.printdata()
        