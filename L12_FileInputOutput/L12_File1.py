#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:30:07 2021

@author: ramanathanmuthuganapathy
"""


#File input and output

# Write / read text data

msg1 = 'This is message 1 \n'
msg2 = 'This is a course on Data Science \n'
msg3 = 'The course number is ED5340 \n'

f = open('messages.txt', 'w') #Opens a file for writing
f.write(msg1) #Writes a new string 
f.write(msg2)
f.write(msg3)
f.close() #Closes the opened file

f = open('messages.txt', 'r')  #Opens a file for reading
data = f.read() #Reads ALL lines into data
print(data)
print(type(data))
f.close()

#Other write functions

#msg4 = ['New\n', 'Course\n']
msg4 = 'A new course\n'
msg5 = ['New\n', 'Course\n']
f = open('messages.txt', 'w')
f.write(msg4)
f.writelines(msg5)
f.close()

#Needs to be converted to strng before writing
tup = ('Ram', 23, 1456)
lst = [12, 23, 34]
dct = {'Name' : 'Raman', 'Roll' : 123}
tup1 = ('Ram1', 123, 14516)
lst1 = [121, 213, 341]
dct1 = {'Name1' : 'Raman1', 'Roll1' : 1123}
f = open('messages.txt', 'w')
f.write(str(tup))
f.write(str(lst))
f.write(str(dct))
f.write('\n')
f.write(str(tup1))
f.write(str(lst1))
f.write(str(dct1))
f.close()

f = open('messages.txt', 'r')
data = f.read() # reads all the contents and returns a string
print(data)

f.seek(0)
data = f.read(10) # reads 10 characters
print(data)
print(type(data))
f.seek(0)
data = f.readline()
print(data)
f.seek(0)
data = f.readlines()
data = list(data)
print(data)
print(type(data))
f.close()

#numbers (are written as strings)
f = open('numbers.txt', 'w+') # writing and reading
f.write(str(1234))
f.write('\n')
#f.write(123.45)
f.write(str(123.45))
f.seek(0)
a = int(f.readline())
b = float(f.readline())
print(a, b)

with open('messages.txt', 'r') as f: #with closes the file automatically
    data = f.read()
print('using with to open the file')
print(data)