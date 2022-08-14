#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:09:40 2020

@author: ramanathanmuthuganapathy
"""


# To give examples of dictionary and accessing its elements

dct1 = {20 : 100, 10 : 200, 'ED2' : 'name1', 'ED1' : 'name2'} 

print('Printing the entire dictionary : ', dct1)

print('Printing using the key values ; ', dct1[10], dct1['ED1'])

print('\n')
print('Using Iterator over key-value pairs');
for k, v in dct1.items():
    print(k, v)

print('\n')
print('Iterate over keys: prints only keys');
for k in dct1.keys():
    print(k)

print('\n')
print('Iterate over the dictionary, prints only keys');
for k in dct1:
    print(k)

print('\n')
print('Iterate over values, prints only values');
for v in dct1.values():
    print(v)

print('\n')
print('Iterate over keys and printing the key, value');
for k in dct1.keys():
    print(k, dct1[k])
    
print('\n')
lst = [30, 20, 10]
tup = ((0, 'Raman'), (213, 'Anand'), (40, 'Sid'), (50, 'Bits'))
print(type(tup))
#dct2 = dict.fromkeys(lst, value = lambda x : x[1])
dct2 = dict.fromkeys(lst, 24)
# dict.from
print('using a sequence for creating dictionary',dct2)
dct3 = dict.fromkeys(tup, 24)
print('using a tuple for creating dictionary',dct3)
lst2 = [46, 46, 37]

    