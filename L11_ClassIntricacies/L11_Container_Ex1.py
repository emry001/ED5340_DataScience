#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:31:43 2021

@author: ramanathanmuthuganapathy
"""


#To demonstrate class containership

#Faculty has a department
#Student has a department

class Department:
    def __init__(self, dname = 'EnggDesign'):
        self._deptname = dname

    def print_dept(self):
        print(self._deptname)
        
class Faculty:
    def __init__(self, dept, fname = 'Raman', fid = '1234'):
        self._fname = fname
        self._fid = fid
        self._dobj = Department(dept)
        
    
    def print_faculty(self):
        print(self._fname, self._fid)
        self._dobj.print_dept()
        
f1 = Faculty('Engg. Design', 'Ramanathan', '12')
# f1.print_faculty()

f2 = Faculty('ED', 'Name1', '23')
f3 = Faculty('ME', 'Name2', '34')
f4 = Faculty('BT', 'Name3', '45')

#List of faculty
lstofFac = []
lstofFac.append(f1)
lstofFac.append(f2) 
lstofFac.append(f3)
lstofFac.append(f4)

for each in lstofFac:
    each.print_faculty()
    