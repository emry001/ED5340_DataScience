#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 22:17:55 2021

@author: ramanathanmuthuganapathy
"""

import random

class Matrix:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.mat = [[random.randint(1,10) for j in range(self.col)] for i in range(self.row)]
        print(type(self.mat))
        
    def AddMatrices(self, other, zipfn = False):
        matC = Matrix(self.row, self.col)
        matC.mat = [[self.mat[i][j] + other.mat[i][j] for j in range(self.col)] for i in range(self.row) ]
        
        # it = zip(self.mat, other.mat)
        # for iter in it:
        #     print(*iter)
        #     it1 = zip(*iter)
        #     for each in it1:
        #         print(each)
        
        if (zipfn):        
            matC = [[sum(each) for iter in zip(self.mat, other.mat)]            for each in zip(*iter)]
            
        return matC
        
    def MultMatrices(self, other):
        # it = zip(*other.mat)
        # for each in it:
        #     print(each)
        #     print(*each)
            
        # for ele in self.mat:
        #     print(ele)
        #     it = zip(*other.mat)
        #     for each in it:
        #         print(each)
        #         s = 0
        #         for (a,b) in zip(ele, each):
        #            s = s+(a*b)
        #         print(s)
        matC = Matrix(self.row, self.col)        
        matC.mat = [[sum(a *b for (a,b) in zip(ele, each))  for each in zip(*other.mat)] for ele in self.mat]
        return matC
                
    def ScaleMatrix(self, scale = 1):
        matC = Matrix(self.row, self.col)   
        lst = []
        for ele in self.mat:
            # print(ele)
            lst1 = map(lambda n : scale * n, ele)
            #NOTE: return from map function has to be converted to a list.
            lst.append(list(lst1))
        
        matC.mat = lst
        return matC
    
    def print_matrix(self):
        print(self.mat)

#derived class
        
class Matrix1(Matrix):
    def __init__(self, r, c):
        super().__init__(r, c)
    
    def PowerMatrix(self, power = 1):
         matC = Matrix1(self.row, self.col) 
         if power <= 1:
             print('value of power should be greater than 1')
             return self
         
         for i in range(1, power):
             matC = self.MultMatrices(self)
             self = matC
             
         return matC
         

#Using the base class       
m1 = Matrix(3, 3)
m2 = Matrix(3, 3)

m3 = m1.AddMatrices(m2)

m1.print_matrix()
m2.print_matrix()
m3.print_matrix()
m4 = m1.MultMatrices(m2)
m4.print_matrix()
m5 = m1.ScaleMatrix(2)
m5.print_matrix()

#Using the derived class
#Power of a matrix
m6 = Matrix1(3, 3)
print(type(m6))
# for i in range(1):
#     m7 = m6.MultMatrices(m6)
#     m6 = m7
    
# m7.print_matrix()
#m7 = Matrix(3, 3)
m7 = m6.PowerMatrix(2)
m7.print_matrix()