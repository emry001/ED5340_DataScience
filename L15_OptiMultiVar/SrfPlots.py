#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:32:37 2021

@author: ramanathanmuthuganapathy
"""


from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math

pi = np.pi

# The following will print a 3D surface
global optionval
def Plot3DSrf():
    
    if optionval >= 3:
        x = np.arange(-1.0, 1.0, 0.1)
        y = np.arange(-1.0, 1.0, 0.1)
    elif optionval == -1:
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.linspace(0, 2 * np.pi, 100)
    else:
        # x = np.arange(-70.0, 70.0, 0.5)
        # Following x and y for Himmelblau
        # x = np.arange(-4.0, 4.0, 0.1)
        # y = np.arange(-4.0, 4.0, 0.1)
        x = np.arange(-4.0, 8.0, 0.1)
        y = np.arange(-4.0, 8.0, 0.1)
        
    W1,W2 =np.meshgrid(x,y) #Forming MeshGrid
    if optionval == 1:
        J = MinSrf(W1, W2)
        # J = HimmelblauFn(W1, W2)
    elif optionval == 2:
        J = MaxSrf(W1, W2)
    elif optionval == 3:
        J = SaddleSrf(W1, W2)
    elif optionval == 4:
        J = SaddleSrf2(W1, W2)
    elif optionval == 5:
        J = MaxSrf2(W1, W2)
    elif optionval == 6:
        J = MinSrf2(W1, W2)
    else:
        J = SinSrf(W1, W2)
        
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot_surface(W1, W2, J, alpha = 0.5)
    
    ax.set_xlabel('W1')
    ax.set_ylabel('W2')
    ax.set_zlabel('J(W1,W2)')
    
    plt.show()
    
    fig = plt.figure(figsize=(5, 5))
    # lst = [num for num in range(0, 40, 2)]
    cp  = plt.contour(x, y, J, levels=20)
    plt.clabel(cp, fontsize=8)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

    plt.show()

def MinSrf(W1, W2):
    return (W1-2)**2 + (W2-2)**2

def MaxSrf(W1, W2):
    return -(W1-2)**2 - (W2-2)**2.

def SaddleSrf(W1, W2):
    return (W1)**2 - (W2)**2

def SaddleSrf2(W1, W2):
    return (W1)**3 - 3*W1*(W2)**2

def MaxSrf2(W1, W2):
    return -4*(W1)**2 - (W2)**2

def MinSrf2(W1, W2):
    return 4*(W1)**2 + (W2)**2

def SinSrf(W1, W2):
    return np.sin(W1)*np.sin(W2)

def HimmelblauFn(W1, W2):
    return ((W1**2 + W2 - 11)**2 + (W1 + W2**2 - 7)**2)

optionval = int(input('Enter 1 for min, 2 for max, 3 for saddle1, 4 for Saddle2, 5 for MaxSrf2,6 for MinSrf2, -1 for SinSrf: '))

Plot3DSrf()

# #Horse saddle 
# x = np.arange(-1.0, 1.0, 0.1)
# y = np.arange(-1.0, 1.0, 0.1)
# W1,W2 =np.meshgrid(x,y) #Forming MeshGrid
# # J = (W1)**2 + (W2)**3
# J = (W1)**2 - (W2)**2
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# ax.plot_surface(W1, W2, J)

# ax.set_xlabel('W1')
# ax.set_ylabel('W2')
# ax.set_zlabel('J(W1,W2)')

# plt.show()