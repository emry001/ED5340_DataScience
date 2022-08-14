#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:36:33 2021

@author: ramanathanmuthuganapathy
"""


#class studentdetail

class StudentDetail:
    
    #Data but public
    #Self is like 'this' pointer
    def datainput(self, n, r, s):
        self.name = n
        self.rollno = r
        self.sem = s

    #Data is private    
    def datainput1(self, n, r, s):
        self._name1 = n
        self._rollno1 = r
        self._sem1 = s

    #Constructor
    def __init__(self, n='', r=1, s=1):
        self.name = n
        self.rollno = r
        self.sem = s
        
    #Printing the data
    def printout(self):
        print(self.name, self.rollno, self.sem)
        
    #Printing the data
    def printout1(self):
        print(self._name1, self._rollno1, self._sem1)
        
    #destructor
    def  __del__(self):
        print('Del obj' + str(self))
        
s1 = StudentDetail() #Object instantiation
s1.datainput('Ram', 12, 3)
s1.printout()
print('name = ', s1.name, 'rollno = ', s1.rollno, 'sem = ', s1.sem)
s2 = StudentDetail('Shyam', 23, 34) #Another object using constructor
s2.printout()
#Data is strictly not private
print('name = ', s2.name, 'rollno = ', s2.rollno, 'sem = ', s2.sem)
#changing name member of S2
s2.name = 'Ramanathan'
print('name = ', s2.name, 'rollno = ', s2.rollno, 'sem = ', s2.sem)

s3 = StudentDetail()
s3.datainput1('Sham', 83, 345) 
s3.printout1()
#name1 is a private data. use _
s3._name1 = 'Ramesh'
s3.printout1()