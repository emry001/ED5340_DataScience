#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 06:50:38 2021

@author: ramanathanmuthuganapathy
"""


class StudentDetail:
    
    #Data but public
    #Self is like 'this' pointer
    # def datainput(self, n, r, s):
    #     self._name = n
    #     self._rollno = r
    #     self._sem = s
        
    #Constructor
    def __init__(self, n='R', r=1, s=1):
        self._name = n
        self._rollno = r
        self._sem = s
        
    #Printing the data
    def printout(self):
        print('name = ', self._name, ", " , 'roll no = ',  self._rollno, ", " , 'sem = ', self._sem)
        
    #destructor
    def  __del__(self):
        print('Del obj' + str(self))
        
    
s1 = StudentDetail()
s1.printout()

s1 = StudentDetail('Ram')
s1.printout()

s1 = StudentDetail('Raman', 23)
s1.printout()

s1 = StudentDetail('Ramana', 23, 5)
s1.printout()