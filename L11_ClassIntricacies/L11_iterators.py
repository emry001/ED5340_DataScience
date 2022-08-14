#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:25:05 2021

@author: ramanathanmuthuganapathy
"""


st = 'Raman'
it = st.__iter__()
#help(str.__next__)
print(type(it))
#help(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

for it in st:
    print(it, type(it))
    
class Iterator:
    def __init__(self, data):
        self.data = data
        self.len = len(data)
        self.start = 0
        self.end = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.end == self.len:
            raise StopIteration
            
        self.data1 = self.data[self.end]
        self.end += 1
        return self.data1
    
lst = [10, 20, 30]

it = Iterator(lst)
for each in it:
    print(each)