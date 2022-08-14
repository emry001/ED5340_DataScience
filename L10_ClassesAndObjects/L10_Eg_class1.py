#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:55:28 2020

@author: raman
"""


#Classes and objects
class Employee:
    def set_data(self, n, a, s):
        self._name = n
        self._age = a
        self._salary = s
        
    def disp_data(self):
        print(self._name, self._age, self._salary)
        
e1 = Employee()   #Object instantiation
e1.set_data('Raman',23, 45.5)
e1.disp_data()

e2 = Employee()
e2.set_data('Vid',23,453.2)
e2.disp_data()

#you can use anyother word other than self

class Employee1:
    def set_data(self1, n, a, s): #self1 contains the address of E1
        self1._name = n
        self1._age = a
        self1._salary = s
        
    def disp_data(self2): #Self2 contains the address of E1
        print(self2._name, self2._age, self2._salary)
        
E1 = Employee1() # nameless address and stored in E1
E1.set_data('Raman1', 233, 3456) #When the method is called, address of E1
#is send and collected in self1
E1.disp_data() #When this method is called, addreass of E1 is collected 
#self2. Basically, self1 and self2 contains the address of E1 whent the 
#method is called.

#HOWEVER, THE FOLLOWING DOES NOT WORK, where self is not the first one but
#the last one!

#class Employee2:
#    def set_data(n, a, s, self):
#        self._name = n
#        self._age = a
#        self._salary = s
        
#    def disp_data(self):
#        print(self._name, self._age, self._salary)

#Emp1 = Employee2()
#Emp1('Test', 23, 345)

#Object initialization

class EmployeeInit:
    def set_data(self, n, a, s):
        self.name = n
        self.age = a
        self.salary = s
    
    def disp_data(self):
        print(self.name, self.age, self.salary)
        
    def __init__(self, n = 'R', a= 0, s= 14.5):
        self.name = n
        self.age = a
        self.salary = s
        
    def __del__(self):
        print('Deleting object' + str(self))
        
Emp1 = EmployeeInit()
Emp1.disp_data()
Emp2 = EmployeeInit('Ramu', 23, 345.5)
Emp2.disp_data()
        
        
        
class Fruit:
    count = 0
    def __init__(self, name = '', size = 0, color = ''):
        self.name = name
        self.size = size
        self.color = color
        Fruit.count += 1
    
    def display():
        print(Fruit.count)
        
f1 = Fruit('Banana', 23, 'Yellow')

print(vars(f1))
print('\n')
print(dir(f1))

    
    
    
    
    
    
        