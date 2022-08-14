#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 00:04:40 2021

@author: ramanathanmuthuganapathy
"""


#To demonstrate Multi-level inheritance

class Base:
    def __init__(self, name):
        self._name = name
        print('Inside base constructor')
          
    def printbase(self):
        print('Inside base print')
        print(self._name)
        
    def __del__(self):
        print('Inside the destructor of base')
    
class Derived1(Base):
    def __init__(self, name):
        super().__init__(name)
        print('Inside derived1 constructor')
    
    def printderived1(self):
        print('Inside derived1 print')
        print(self._name)
    
    def __del__(self):
        #super().__del__()
        print('Inside the destructor of Derived1')
        
class Derived2(Derived1):
    def __init__(self, name):
        super().__init__(name)
        print('Inside derived2 constructor')
    
    def printderived2(self):
        print('Inside derived2 print')
        #self.printderived1()
        #Derived2.printderived1(self)
        #super().printderived1()
        print(self._name)
        
    def __del__(self):
        #super().__del__()
        print('Inside the destructor of Derived2')
        
d2 = Derived2('Ram')
d2.printderived2()
d2.printderived1()
d2.printbase()

#d1 as object of derived one
d1 = Derived1('Raman')
#d1.printderived2() #cannot be done
d1.printbase()

