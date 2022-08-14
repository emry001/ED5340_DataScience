#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:10:49 2020

@author: ramanathanmuthuganapathy
"""


#To demostrate nested dictionary and unpacking operator

studlist = {'Anand' : {'DOB' : '20/11/2001', 'Roll' : 'ED1234' },
'Ramesh' : {'DOB' : '19/11/2001', 'Roll' : 'ED1235' },
'Kamesh' : {'DOB' : '21/11/2001', 'Roll' : 'ED1236' } }
''
print('printing the nested list', studlist)

for k in studlist.keys():
    print(k, studlist[k])

print('\n')    
print('Printing only the DOBs : ')
for v in studlist.values():
    print(v['DOB'])
    
    
print('\n')    
print('Printing only the DOBs of each name: ')
for k, v in studlist.items():
    print('DOB of', k, 'is ', v['DOB'])
    
    
namelist = {'name1' : 'Anand', 'name2' : 'Ramesh', 'name3' : 'Kamesh'}
print('\n') 
print('Unpacking using * - will give only the keys')
print(*namelist)


print('\n') 
print('Unpacking using **')
namelist1 = {**namelist}
print(namelist1)

print('\n') 
print(*studlist)
studlist1 = {**studlist}
print(studlist1)

print('\n') 
print('Printing the keys of the values of studlist')
for v in studlist.values():
    print(*v)
    #print(**v)
 
print('\n') 
print('Printing the keys and values of the values of studlist')
for v in studlist.values():
    #print(*v, v.values())
    #print(v.keys(), v.values(), v.items())
    print(type(v))
    dct = dict(v)
    for a in v.keys():
        print(dct[a])