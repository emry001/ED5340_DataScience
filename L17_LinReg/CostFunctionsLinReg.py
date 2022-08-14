#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 22:21:56 2021

@author: ramanathanmuthuganapathy
"""

from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math

class CostFunLR:
    def __init__(self):
        self.x = np.array([0, 1, 2, 3, 4])
        self.y = np.array([0, 1, 2, 3, 4])
        self.w0 = np.arange(-3.0, 3.0, 0.1)
        self.w1 = np.arange(-3.0, 3.0, 0.1)
        for i in range(len(self.x)): 
            print(self.x[i], self.y[i])
            
    def ComputeCostFn(self, TwoD = True):
        J = []
        
        w0 = self.w0
        w1 = self.w1
        x = self.x
        y = self.y
        J1 = np.zeros((len(w0+1), len(w1+1)))
        if (TwoD):
            for j in range(len(w1)):
                w2 = []
                for i in range(len(x)): 
                    w2.append((w1[j]*x[i] - y[i])**2)
                J.append(sum(w2))
            return w1, J
        else:
            for k in range(len(w0)):
                lst = []
                for j in range(len(w1)):
                    # print(w0[k], w1[j])
                    w2 = []
                    for i in range(len(x)): 
                        w2.append((w0[k] + w1[j]*x[i] - y[i])**2) 
                    lst.append(sum(w2)/(2*len(x)))
                    if w0[k] == 0.0 and w1[j] == 1.0:
                        print(sum(w2)/(2*len(x)))
                    J1[j][k] = sum(w2)/(2*len(x))
                
            return w0, w1, J1
    
        
    def plot2d(self):
        w1, J = self.ComputeCostFn(True)
        fig, ax = plt.subplots()
        ax.plot(w1, J)
        
        ax.set(xlabel='W1 vlues', ylabel='J(w1)',
               title='Cost function J(w1) = (W1*X - Y)^2')
        ax.grid()
        
        # fig.savefig("test.png")
        plt.show()
    def plot3d(self):
        w0, w1, J = self.ComputeCostFn(False)
        print(type(J))
        W0,W1 =np.meshgrid(w0,w1) #Forming MeshGrid
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        ax.plot_surface(W0, W1, J, alpha = 0.5)
        
        ax.set_xlabel('W0')
        ax.set_ylabel('W1')
        ax.set_zlabel('J(W0,W1)')
        
        plt.show()
        
        
        # fig = plt.figure(figsize=(8, 8))
        # cp  = plt.contour(w0, w1, J, levels=50)
        fig, ax = plt.subplots(1, 1, figsize = (6,6))
        lst = [num for num in range(-4, 100, 5)]
        # cp  = ax.contour(w0, w1, J, levels=lst)
        cp  = ax.contour(W0, W1, J, levels=40)
        ax.plot(0, 1, 'o', color='orange')
        ax.clabel(cp, fontsize=8)
        ax.set_xlabel('W0')
        ax.set_ylabel('W1')
        # ax.set(xlabel='x vlues', ylabel='y values',
        # title='Explicit function y = f(x)')
        
        plt.show()
    
J1 = CostFunLR()
J1.plot2d()
J1.plot3d()