#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 22:02:59 2021

@author: ramanathanmuthuganapathy
"""


from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#plotting y = x^2
z = np.arange(-8.0, 8.0, 0.01)
si = 1.0 / (1+np.e**(-z*100))

fig, ax = plt.subplots()
ax.plot(z, si)

ax.set(xlabel='z values', ylabel='sigma(z)',
       title='Sigmoid / logistic function')
ax.grid()

# fig.savefig("test.png")
plt.show()

#-log function
z = np.arange(0.01, 1.0, 0.01)
lo = -np.log(z)

fig, ax = plt.subplots()
ax.plot(z, lo)

ax.set(xlabel='values', ylabel='-log',
       title='-log function')
ax.grid()

# fig.savefig("test.png")
plt.show()

z = np.arange(0.01, 1.0, 0.01)
lo = -np.log(1-z)

fig, ax = plt.subplots()
ax.plot(z, lo)

ax.set(xlabel='values', ylabel='-log(1-z)',
       title='-log(1-z) function')
ax.grid()

# fig.savefig("test.png")
plt.show()