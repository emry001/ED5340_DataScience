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

def plot2d(w1, J):
    fig, ax = plt.subplots()
    ax.plot(w1, J)
    
    ax.set(xlabel='W1 vlues', ylabel='J(w1)',
           title='Cost function J(w1) = (W1*X - Y)^2')
    ax.grid()
    
    # fig.savefig("test.png")
    plt.show()
    
x = np.arange(0.0, 4.0, 1)
# y = np.arange(0.0, 5.0, 1)
y = np.array([0, 1, 2, 3, 4])
z = y**2
print(z)
w1 = np.arange(-2.0, 4.0, 0.25)

J = []
for j in range(len(w1)):
    w2 = []
    for i in range(len(x)): 
        w2.append((w1[j]*x[i] - y[i])**2)
    J.append(sum(w2))
print(J)

plot2d(w1, J)