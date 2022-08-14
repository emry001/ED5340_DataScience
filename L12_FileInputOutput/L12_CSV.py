#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:53:22 2021

@author: ramanathanmuthuganapathy
"""


import csv

with open('test_csv1.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Header names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and handles {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    

with open('test_data_csv1.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    x = []
    y = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is x-data and {row[1]} is y-data.')
            x.append(int(row[0]))
            y.append(int(row[1]))
            line_count += 1
    print(f'Processed {line_count} lines.')
    print(x, y)