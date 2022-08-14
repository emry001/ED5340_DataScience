#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:31:02 2021

@author: ramanathanmuthuganapathy
"""

def fun():
    print('Inside fun')

class Example:
    def __init__(self, n='', r=''):
        self._name = n
        self.__roll = r
        
    def print_details(self):
        print(self._name, self.__roll)
        
    def show():
        print('Inside show: class method')
        fun()
        
e1 = Example()
e2 = Example('Ram','2345')
e1._name = 'Ramana'
e1.__roll = '1234'
e1.print_details()
e2.print_details()

Example.show()


        