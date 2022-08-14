#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:44:56 2021

@author: raman
"""


#To demonstrate accessibility

class Base:
    def __init__(self, name, roll, marks):
        self.name = name
        self._roll = roll
        self.__marks = marks
    
    def samename(self):
        print('Inside same name of base')
        
    def printbase(self):
        print(self.name, self._roll, self.__marks)
        
class Derived(Base):
    def __init__(self, name, roll, marks, name1, roll1, marks1):
        super().__init__(name, roll, marks)
        self.name1 = name1
        self._roll1 = roll1
        self.__marks1 = marks1
        print('Inside init', id(self.__marks1))
        # changing the details of the base
        self.name = 'Newname'
        self._roll = 4356
        self.__marks = 89
        
    def samename(self):
        print('Inside same name of derived')
        
    def printderived(self):
        super().printbase()
        print(self.name1, self._roll1, self.__marks1)
        print(self.name, self._roll, self.__marks)
        
d1 = Derived('Ram', 1234, 85, 'Raman', 4356, 76)
d1.printderived()
d1.name1 = 'Ramamoorthy'
d1._roll1 = 8890
d1.__marks1 = 10  #Cannot change this
print('outside init', id(d1.__marks1))

d1.name = 'Siva'
d1._roll = 34566
d1.__marks = 23
d1.printderived()

d1.samename()

print('Just printing')
print(d1.name1, d1._roll1, d1.__marks1)
print(d1.name, d1._roll, d1.__marks)      