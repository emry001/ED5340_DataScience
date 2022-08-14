#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 08:28:04 2020

@author: raman
"""

import random
class Matrix:
    def __init__(self, row, col, mat):
        self.row = row
        self.col = col
        self.mat = [[random.randint(1,10) for j in range(col)] \
                    for i in range(row)]
    
    def add_mat(mat1, mat2, zipfn = False):
        if (not zipfn):
            mat3 = [[(mat1[i][j] + mat2[i][j]) for j in range(len(mat1[0]))]\
                for i in range(len(mat1))]
        else:
            print('Adding using zip fun')
            mat3 = [[a+b for (a,b) in zip(xrow1, xrow2)] \
                    for (xrow1,xrow2) in zip(mat1,mat2) ]
        return mat3
    
    def mat_mult(mat1_2d, mat2_2d):
        mat3 = [[sum(a * b for (a,b) in zip(x1row, x2row)) \
                     for x2row in zip(*mat2_2d)]\
                    for x1row in mat1_2d]
        return mat3
        
    def __del__(self):
        print('Deleting the object '+ str(self))
        
mat = 0
mat1 =  Matrix(3, 4, mat)
print(mat1.mat) #mat1 is the identifier and mat1.mat isthe 2D matrix

print('*mat1.mat = ',*mat1.mat)
print('mat1.mat[0] = ', mat1.mat[0])
print('mat1.mat[1] = ', mat1.mat[1])
print('mat1.mat[2] = ', mat1.mat[2])

it = zip(*mat1.mat) #iteration for each individual list in mat1.mat
#Print the inverse of a matrix
for item in it:
    print(item)
    
mat2 = Matrix(3,4,mat)
print(mat1.mat) 
print(mat2.mat)

#Adding two matrices
mat3 = Matrix(3,4,mat)
mat3.mat = Matrix.add_mat(mat1.mat, mat2.mat)
print('Addition of two matrice = ', mat3.mat)

#Adding two matrices
mat3 = Matrix(3,4,mat)
mat3.mat = Matrix.add_mat(mat1.mat, mat2.mat, True)
print('Addition of two matrice using zip fun= ', mat3.mat)

mat4 = Matrix(4,4,mat)
# Creatig mat5 for multiplying mat2 and mat4
mat5 = Matrix(mat2.row, mat4.col, mat)
mat5.mat = Matrix.mat_mult(mat2.mat, mat4.mat)
print('Result of matrix multiplication = ', mat5.mat)
