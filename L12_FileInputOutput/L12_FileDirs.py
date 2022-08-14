#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:24:25 2021

@author: ramanathanmuthuganapathy
"""


#File and directory operations

import os

import shutil

print(os.name)
print(os.getcwd())
print(os.listdir('.'))
print(os.listdir('..'))


if os.path.exists('TestDir'):
    print('TestDir exists')
else:
    os.mkdir('TestDir')
    
os.chdir('TestDir')
print(os.getcwd())
# os.makedirs('./dir2/dir3') #Recursive directory creation

f = open('myfile', 'w')
f.write('This is a created file')
f.close()
stats = os.stat('myfile')
print(stats.st_size)

os.rename('myfile', 'Yourfile')
shutil.copyfile('yourfile', 'ourfile')
os.remove('yourfile')

curpath = os.path.abspath('.')
print(curpath)
os.path.join(curpath, 'yourfile')
if os.path.isfile(curpath):
    print('Your file exist ')
else:
    print('Your file does not exist')