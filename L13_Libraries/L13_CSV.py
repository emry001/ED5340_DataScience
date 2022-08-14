#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 12:02:59 2021

@author: ramanathanmuthuganapathy
"""


import pandas as pd

#Using Pandas
df = pd.read_csv('test_data_csv11.csv')
print(df)
print(df['X'])
lst = df['X']
print('Printing the list')
print(lst, type(lst))
print('printing each element')
for each in lst:
    print(each)
print(lst[1])
# print(df['X'][0])
#Using usecols
df = pd.read_csv('test_data_csv11.csv', usecols=['X'])
print(df)
df = pd.read_csv('test_data_csv11.csv',usecols=['Y'])
print(df)
#Using index_col (using that column as index)
df = pd.read_csv('test_data_csv11.csv', index_col='X')
print(df)
df = pd.read_csv('test_data_csv11.csv',index_col='Y')
print(df)
# df = pd.read_csv('data.csv')
# print(df)
# df = pandas.read_csv('test_data_csv1.csv', index_col='Y')
# print(df)
# print(df['X'][0], type(df['X'][0]))

