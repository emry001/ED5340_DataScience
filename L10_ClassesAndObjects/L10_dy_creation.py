#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:53:50 2021

@author: ramanathanmuthuganapathy
"""


# Dynamic creation of attributes

class Passbook:
    pass

    def printout(self):
        print(self.name, self.num)
        
    def printwithargs(*args):
        for each in args:
            print(each)
        
        
p1 = Passbook()
p1.name = 'Ram'
p1.num = 12345
p1.printout()
print(p1.name, id(p1.name))

p1.name='Raman'
print(p1.name, id(p1.name))
Passbook.printwithargs(p1.name, p1.num)
p2 = Passbook()
p2.name = 'Ram'
p2.num = 12345
p2.bal = 2345
p2.printout()

del p2.bal

p2.printout()