#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:27:19 2021

@author: raman
"""


# To demonstrate the derived from base class

class Base:
    def __init__(self, name):
        self.name = name
        print('Inside the base class constructor')
        
    def printbase(self):
        print(self.name)
        
class Derived(Base):
    def __init__(self, roll, name):
        super().__init__(name)  #No need for self again
        self.roll = roll
        print('Inside the derived class constructor')
        
    def printderived(self):
        print(self.roll)
        print(self.name) #Derived class can access the 
        #variables of the base class but not vice versa
    
d1 = Derived(50, 'R')
d1.printderived()
# d1.printbase() #derived can access the methods of base
#b1 = Base('Ram')