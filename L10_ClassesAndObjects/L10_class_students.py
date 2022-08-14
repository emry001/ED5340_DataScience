#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 08:30:39 2020

@author: raman
"""


#THis program deals with a program on students 

class Students:
    StudentsLst = []
    def __init__(self, name = '', rollno = 10, marks = 80):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        
    def display_stud(self):
        print(self.name, self.rollno, self.marks)
        
    def comput_avg_max_min(self):
        ma = max(self.marks)
        mi = min(self.marks)
        avg = sum(self.marks)/5
        self.marks.sort()
        
        return ma, mi, avg
        
    def __eq__(self, other):
        if self.name == other.name and self.rollno == other.rollno \
            and self.marks == other.marks:
            return True
        else:
            return False
#Creating a list of students
#For five subjects 
C1 = Students('Raman', 100, [0,45,70,80,90])
C1.display_stud()
        
#data as list for few students
StudLst = [] #This identifier is outside the class
C2 = Students('Ram', 100, [0,85,70,80,90])
StudLst.append(C2)
C2 = Students('Vid', 200, [0,45,40,30,90])
StudLst.append(C2)
C2 = Students('Sah', 300, [0,55,70,60,90])
StudLst.append(C2)
C2 = Students('Sri', 300, [20,15,70,40,90])
StudLst.append(C2)
for data in StudLst:
    data.display_stud()
#Clearing the list StudLst
del(StudLst[:])

#Now, adding an identifier inside the class and creating methods
C2 = Students('Name1', 100, [0,85,70,80,90])
Students.StudentsLst.append(C2)
C2 = Students('Name2', 200, [84,35,40,20,90])
Students.StudentsLst.append(C2)
C2 = Students('Name3', 300, [100,45,70,60,90])
Students.StudentsLst.append(C2)
C2 = Students('Name4', 400, [40,25,20,80,90])
Students.StudentsLst.append(C2)

for data in Students.StudentsLst:
    data.display_stud()
    ma, mi, avg = data.comput_avg_max_min()
    print(ma, mi, avg)
    print('sorted marks : ', data.marks)

#Clearing the list Students.StudentsLst
del(Students.StudentsLst[:])


C2 = Students('Name1', 100, [0,85,70,80,90])
Students.StudentsLst.append(C2)
(Students.StudentsLst[0]).display_stud()

#Clearing the list Students.StudentsLst
del(Students.StudentsLst[:])


#Reading from a file
fin = open('Stud.txt', 'r')
while True:
    
    C1 = Students()
    data = fin.readline() #Read line by line
    if data == '':
        break
    data1 = data.split(' ')
    for i in range(len(data1)):
        print(i, data1[i])
    
    name = data1[0]
    roll = int(data1[1])
    marks = data1[2:len(data1)]
    for i in range(len(marks)):
        marks[i] = float(marks[i])
    
    C1 = Students(name, roll, marks)
    Students.StudentsLst.append(C1)
    #C2 = set(Students(name, roll, marks))
    
#for data in C2:
#    print(data)

for data in Students.StudentsLst:
    data.display_stud()
    ma, mi, avg = data.comput_avg_max_min()
    print(ma, mi, avg)
    print('sorted marks : ', data.marks)

#Testing list equal or not  
lst1 = [10,20,30]
lst2 = [10,20,30]

if lst1 == lst2:
    print('they are equal')


if Students.StudentsLst[0].marks == Students.StudentsLst[1].marks:
    print('Two students marks are equal')
else:
    print('they are unequal')
    
#Comparing the classes as well - NOT WORKING FOR CLASSES - Use Operator
#Overloading
if Students.StudentsLst[0] == Students.StudentsLst[1]:
    print('The two classes are equal - using operator overloading')
else:
    print('The classes are unequal - using OO')