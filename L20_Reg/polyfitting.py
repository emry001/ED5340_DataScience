#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 07:47:03 2021

@author: ramanathanmuthuganapathy
"""


from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def polyfitfn(x, x1, y, deg=1):
    wts = np.polyfit(x, y, deg)
    #Imp NOTE: wts[0] belong to the highest degree.
    ip = 0 #interpolated points
    d = deg
    for i in range(0,deg+1):
        c = wts[i]*x1**d
        d -= 1
        ip += c
    return wts, ip



# from numpy.polynomial import Chebyshev
x = np.linspace(0, 10, 7)
y = np.array([2.2, 3.0, 3.45, 6.2, 7.86, 9.23, 10.33])
print(y)

plt.figure(figsize=(6,3))
plt.plot(x,y,'o', color='orange')
plt.legend(loc='upper left', fontsize = 8, ncol=1)
plt.xlabel('size')
plt.ylabel('value')
# c = Chebyshev.fit(x, y, deg=2)

x1 = np.linspace(0, 10, 50) #Just increasing the points for plotting
wts, y1 = polyfitfn(x, x1, y, 2)
print(y1, type(y1))
#Plotting using coefficients from polyfit for 2nd degree

# y1 = c[2] + c[1]*x + c[0]*x**2

plt.figure(figsize=(6,3))
plt.plot(x,y,'o', color='orange')
plt.plot(x1, y1, '-', color='cyan', label = 'd=2')
plt.legend(loc='upper left', fontsize = 8, ncol=1)
plt.xlabel('size')
plt.ylabel('value')

plt.show()
#Plotting using coefficients from polyfit for 3rd degree

wts, y1 = polyfitfn(x, x1, y, 3)
# print(y1)
plt.figure(figsize=(6,3))
plt.plot(x,y,'o', color='orange')
plt.plot(x1, y1, '--', color='green', label = 'd=3')
plt.legend(loc='upper left', fontsize = 8, ncol=1)
plt.xlabel('size')
plt.ylabel('value')

# #Plotting using coefficients from polyfit for 4th degree
wts, y1 = polyfitfn(x, x1, y, 4)
# print(y1)
plt.figure(figsize=(6,3))
plt.plot(x,y,'o', color='orange')
plt.plot(x1, y1, '--', color='blue', label = 'd=4')
plt.legend(loc='upper left', fontsize = 8, ncol=1)
plt.xlabel('size')
plt.ylabel('value')

#Plotting using coefficients from polyfit for 5th degree

wts, y1 = polyfitfn(x, x1, y, 5)
print(y1)
plt.figure(figsize=(6,3))
plt.plot(x,y,'o', color='orange')
plt.plot(x1, y1, '--', color='red', label = 'd=5')
plt.legend(loc='upper left', fontsize = 8, ncol=1)
plt.xlabel('size')
plt.ylabel('value')

# Changing the weights can smoothen the curve
# wts[:] = wts[:]*0.1
# wts[0] = 0.0
# y2 = wts[5]*x1**0 + wts[4]*x1**1 + wts[3]*x1**2 + wts[2]*x1**3 + wts[1]*x1**4 + wts[0]*x1**5

# plt.plot(x1, y2, '--', color='yellow', label = 'd=5')

# degree = 6
wts, y1 = polyfitfn(x, x1, y, 6)
print(y1)
plt.figure(figsize=(6,3))
plt.plot(x,y,'o', color='orange')
plt.plot(x1, y1, '--', color='magenta', label = 'd=6')

plt.legend(loc='upper left', fontsize = 8, ncol=1)
plt.xlabel('size')
plt.ylabel('value')

#multiple axis figure
m_fig, m_axes = plt.subplots(1, 3, figsize = (12,4))
ax = m_axes[0]
ax.plot(x,y,'o', color='orange')
ax.set(xlabel='size', ylabel='value',
        title='Data points')

ax = m_axes[1]
wts, y1 = polyfitfn(x, x1, y, 2)
ax.plot(x,y,'o', color='orange')
ax.plot(x1, y1, '-', color='cyan', label = 'd=2')
ax.set(xlabel='size', ylabel='value',
        title='d = 2')

ax = m_axes[2]
wts, y1 = polyfitfn(x, x1, y, 3)
ax.plot(x,y,'o', color='orange')
ax.plot(x1, y1, '-', color='cyan', label = 'd=3')
ax.set(xlabel='size', ylabel='value',
        title='d = 3')

plt.show()

m_fig, m_axes = plt.subplots(1, 3, figsize = (12,4))
ax = m_axes[0]
wts, y1 = polyfitfn(x, x1, y, 4)
ax.plot(x,y,'o', color='orange')
ax.plot(x1, y1, '-', color='cyan', label = 'd=2')
ax.set(xlabel='size', ylabel='value',
        title='d = 4')

ax = m_axes[1]
wts, y1 = polyfitfn(x, x1, y, 5)
ax.plot(x,y,'o', color='orange')
ax.plot(x1, y1, '-', color='cyan', label = 'd=5')
ax.set(xlabel='size', ylabel='value',
        title='d = 5')

ax = m_axes[2]
wts, y1 = polyfitfn(x, x1, y, 6)
ax.plot(x,y,'o', color='orange')
ax.plot(x1, y1, '-', color='cyan', label = 'd=6')
ax.set(xlabel='size', ylabel='value',
        title='d = 6')


plt.show()
