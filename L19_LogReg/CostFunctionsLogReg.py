#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 22:21:56 2021

@author: ramanathanmuthuganapathy
"""
#This file gives the pics for the squared error cost function for logistic regression to demonstrate the non-convexity.

from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math

class CostFunLR:
    def __init__(self):
        self.x = np.array([0, 0.2, 0.4, 0.6, 0.8])
        self.y = np.array([0, 0, 0, 1, 1])
        self.w0 = np.linspace(-10.0, 10.0, 50)
        self.w1 = np.linspace(-10.0, 10.0, 50)
    
#Computes the squared distance cost function with hypothesis function as sigma(z) in ONE or TWO variable(s).    
    def ComputeSDCostFn(self, TwoD = True):
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
                    hypo = w1[j]*x[i]
                    si_hyp = (1 / (1+np.e**(-hypo)))
                    w2.append((si_hyp - y[i])**2)
                J.append(sum(w2)/len(x))
            return w1, J
        else:
            for k in range(len(w0)):
                lst = []
                for j in range(len(w1)):
                    w2 = []
                    for i in range(len(x)): 
                        hypo = w0[k] + w1[j]*x[i]
                        si_hyp = (1 / (1+np.e**(-hypo)))
                        w2.append((si_hyp - y[i])**2) 
                    lst.append(sum(w2))
                    if w0[k] == 0 and w1[j] == 1:
                        print(sum(w2))
                    J1[j][k] = sum(w2)/len(x)
                
            return w0, w1, J1
    
    def ComputeLogLogCostFn(self):
        w0 = self.w0
        w1 = self.w1
        x = self.x
        y = self.y
        J1 = np.zeros((len(w0+1), len(w1+1)))
        print(y)
        for k in range(len(w0)):
            # print('k = ', k, len(w0))
            lst = []
            for j in range(len(w1)):
                w2 = []
                for i in range(len(x)): 
                    hypo = w0[k] + w1[j]*x[i]
                    si_hyp = (1 / (1+np.e**(-hypo)))
                    # print(hypo, si_hyp)
                    costfn1 = - y[i]*np.log2(si_hyp)
                    costfn2 = -(1-y[i])*np.log2(1 - si_hyp)
                    costfn = costfn1 + costfn2
                    w2.append(costfn) 
                lst.append(sum(w2))
                if w0[k] == 0 and w1[j] == 1:
                    print(sum(w2))
                J1[j][k] = sum(w2)/len(x)
                # print(w0[k], w1[j], J1[j][k])
                
        return w0, w1, J1
        
    def plot2d(self):
        w1, J = self.ComputeSDCostFn(True)
        fig, ax = plt.subplots()
        ax.plot(w1, J)
        
        ax.set(xlabel='W1 vlues', ylabel='J(w1)',
               title='Cost function J(w1) = (sigma(W1*X) - Y)^2')
        ax.grid()
        fig.text(0.2, 0, 'Square distance cost function', ha = 'center')
        
        # fig.savefig("test.png")
        plt.show()
    def plot3d(self, logfn=False):
        if(logfn):
            w0, w1, J = self.ComputeLogLogCostFn()
        else:
            w0, w1, J = self.ComputeSDCostFn(False)
        print(type(J))
        # print(J)
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
        fig, ax = plt.subplots()
        lst = [num for num in range(-4, 100, 5)]
        # cp  = ax.contour(w0, w1, J, levels=lst)
        cp  = ax.contour(w0, w1, J, levels=50)
        ax.clabel(cp, fontsize=8)
        ax.set_xlabel('W0')
        ax.set_ylabel('W1')
        # ax.set(xlabel='x vlues', ylabel='y values',
        # title='Explicit function y = f(x)')

        plt.show()
    
J1 = CostFunLR()
# J1.plot2d()
# J1.plot3d()
J1.plot3d(True)