#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 17:12:20 2021

@author: ramanathanmuthuganapathy
"""


#To demonstrate the use of json
#json writes appropriate datatype to a file - serialization

#serialization and deserialization of a list
# IMP: Works only if single type of data is in the file

import json

#Serialization / Deserialization
f = open('jsondata.json', 'w+')
lst = [10, 20, 30]
json.dump(lst, f)
f.seek(0)
inlst = json.load(f)
print(inlst)
print(type(inlst))
f.close()

f = open('jsondata.json', 'w+')
tup = ('Ram', 23, 12345)
json.dump(tup, f)
f.seek(0)
intup = json.load(f) #Returns a list
print(intup)
print(type(intup))
intup1 = tuple(intup)
print(intup1, type(intup1))
f.close()

f = open('jsondata.json', 'w+')
dct = {'Name' : 'Ram', 'Roll' : 1234}
json.dump(dct, f)
f.seek(0)
indct = json.load(f)
print(indct)
print(type(indct))
f.close()

#Dumping as strings
str1 = json.dumps(lst)
str2 = json.dumps(tup)
str3 = json.dumps(dct)
l = json.loads(str1)
t = json.loads(str2)
d = json.loads(str3)
print(l, t, d)
print(type(l), type(t), type(d))

f = open('jsondata.json', 'w')
json.dump(lst, f)
# #json.dump('\n', f)
# f.write('\n')
# json.dump(tup, f)
# f.write('\n')
json.dump(dct, f)
f.seek(0)
f.close()
with open('jsondata.json', 'r') as f:
    l = json.load(f)
    print(l)
    # t = tuple(json.load(f))
    d = json.load(f)
    print(l)
    
# data = f.readline()
# print(list(data))
# print(type(data))

# d = json.load(f)
# print(l, t, d)
# print(type(l), type(t), type(d))