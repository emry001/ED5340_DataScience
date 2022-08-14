#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 20:07:46 2020

@author: raman
"""

import random
#Recap of matrices with zip operator

#row, column = input('Enter row and column : ').split()
row = 2
column = 3
row = int(row)
col = int(column)

#One way to create a matrix
mat1 = [[(i+j) for j in range(col)] for i in range(row)]
print(mat1, type(mat1))

# Creating a 3D array
def create_3D_array(depth,row,col):
    lst = [[[random.randint(1,10) for j in range(col)] for i in range(row)] \
           for k in range(depth)] #mat(depth, row, col) will be output
    return lst

#Second way to create a 2D matrix
def create_2D_mat(row, col):
    mat = [[random.randint(1,10) for j in range(col)] for i in range(row)]
    return mat

mat1 = create_2D_mat(3, 2)
print(mat1)

#Recp of Zip functionn
names = ['Ram','Vid','Ss']
num = [1,2,3]
floats = [1.1,2.2,3.3]

it = zip(names, num, floats) #Takes one from each and creates a list
print(it)
lst = list(it)
print(len(lst))
for item in lst:
    print(item)
    
#Unzipping
n, n1, f = zip(*lst)
print(n, n1, f)

mat2d = create_2D_mat(3, 2)
print(mat2d)

print(mat2d[0], mat2d[1], mat2d[2])
print(*mat2d) #same as above print

mat3d = create_3D_array(2, 3, 2)
print(mat3d)

print(mat3d[0], mat3d[1]) #for two depths, one  list for each
print(*mat3d) #Same as above print
print(*mat3d[0], *mat3d[1]) #*mat[0] dismantles mat[0] into individual lists


mat2d = [[i+j for j in range(len(mat2d[0]))] for i in range(len(mat2d))]
print(mat2d, mat2d[0], mat2d[1], mat2d[2])
#Transpose of a matrix
it = zip(*mat2d)
for item in it:
    print(item)
    
#Multiplication of two matrices
mat1_2d = create_2D_mat(4,3)
mat2_2d = create_2D_mat(3,3)

print('mat1_2d = ', mat1_2d)
print('mat2_2d = ', mat2_2d)

for xrow in mat1_2d:
    print(xrow)
#zip mat1_2d
it = zip(*mat1_2d)
#zip(*mat1_2d) is equal to the following statement
#lst = zip(mat1_2d[0],mat1_2d[1],mat1_2d[2],mat1_2d[3])
#iterates in each of the rows - picks 1st one in each row and then 2nd etc..
#mat1_2d_lst = list(it) # if you do that, then it becomes single list
#print(mat1_2d_lst[0], mat1_2d_lst[1], mat1_2d_lst[2])

mat_mult = [[sum(a * b for (a,b) in zip(x1row, x2row)) for x2row in zip(*mat2_2d)]\
            for x1row in mat1_2d]

print(mat_mult)


