#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:14:36 2021

@author: ramanathanmuthuganapathy
"""


# from matplotlib.figure import Figure
# from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#simple plotting
x = np.linspace(-5, 5, 100)
#plotting y = x^2
y = x**2
# plt.plot(x,y)
# plt.plot(x, y, 'o--')
# plt.plot(x, y, 'o')
# plt.plot(x, y, 'o--', color='red', lw = 2.5, ms = 2)
#plt.plot(x, y, 'o-', color='red', lw = 1.5, ms = 2)
#lw - line width, ms - marker size

#adding figure
plt.figure(figsize=(6,3))
plt.plot(x, y, 'o-', color='red', lw = 1.5, ms = 2, label = 'par. crv')
plt.xlabel('parameter')
plt.ylabel('curve')
# plt.legend(loc='upper right', fontsize = 10)

#plotting y = x^3
x1 = np.linspace(-4 * np.pi, 4 * np.pi, 100)
y1 = np.sin(x1)
plt.plot(x1, y1, '-', color='blue', lw = 1.5, ms = 2, label = 'sin crv')
plt.legend(loc='upper right', fontsize = 10)
# plt.legend(loc='upper right', fontsize = 10, ncol=2)

#using subplots
x = np.arange(-2.0, 2.0, 0.01)
y = x ** 2

#Default is single figure
#fig, ax = plt.subplots()
#single axis
fig, ax = plt.subplots(1, 1, figsize = (4,4))
ax.plot(x, y)
ax.set_xlabel('new x-label')
ax.set_ylabel('new y-label')
ax.set_title('Single axis plot')
# ax.set(xlabel='x vlues', ylabel='y values',
#        title='Explicit function y = f(x)')
ax.grid()
plt.show()

#multiple axis figure
m_fig, m_axes = plt.subplots(2, 2, figsize = (8,4))
ax = m_axes[0][0]
ax.plot(x,y)
ax.set(xlabel='x vlues', ylabel='y values',
        title='Explicit function y = f(x)')
ax = m_axes[0][1]
ax.plot(x1,y1)
ax.set(xlabel='x vlues', ylabel='y values',
        title='Explicit function y = f(x)')
plt.show()

# Parametric curve - https://matplotlib.org/stable/gallery/mplot3d/lines3d.html
# Parametric space curve helix

# Parametric space curve t, t**2, t**3

t = np.arange(-2.0, 2.0, 0.1)
x = t
y = t ** 2
z = t ** 3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('Parametric space curve t, t**2, t**3')

plt.show()

#Changing the above for the contour part
x = np.arange(-2.0, 2.0, 0.1)
y = np.arange(-2.0, 2.0, 0.1)
# The following will print a 3D surface
X,Y=np.meshgrid(x,y) #Forming MeshGrid
#Z = X**3
Z = X **2 + Y ** 2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

# X,Y=np.meshgrid(x,y)
# Z = X **2 + Y ** 2
fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#ax.plot_surface(X, Y, Z)
cp  = plt.contour(x, y, Z)
plt.clabel(cp, fontsize=8)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

plt.show()