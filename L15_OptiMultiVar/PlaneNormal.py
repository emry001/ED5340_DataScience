#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 21:08:32 2021

@author: ramanathanmuthuganapathy
"""

#The code generates some unexpected error but still shows the output.
#Normal at a point on a plane.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# matplotlib inline
import seaborn as sns

# set normal vector, and point on plane
point  = np.array([1, 2, 3])
normal = np.array([1, 1, 2])

# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d = -point.dot(normal)

# create x,y
xx, yy = np.meshgrid(range(10), range(10))

# calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

# setup plot
plt3d = plt.figure(figsize=(10,10)).gca(projection='3d');
plt3d.set_xlabel('x');
plt3d.set_ylabel('y');
plt3d.set_zlabel('z');

# plot the surface
plt3d.plot_surface(xx, yy, z, alpha=0.7);

# plot the point
plt3d.plot([point[0]], [point[1]], [point[2]], color='yellow', marker='o', markersize=10, alpha=0.8);

# set the normal vector to start at the center of the plane
startX = np.mean(plt3d.get_xlim())
startY = np.mean(plt3d.get_ylim())
startZ = (-normal[0] * startX - normal[1] * startY - d) * 1. /normal[2]

# set the normal vector to start at the point on the plane
startX = point[0]
startY = point[1]
startZ = point[2]

# plot the normal vector
plt3d.quiver([startX], [startY], [startZ], [normal[0]], [normal[1]], [normal[2]], linewidths = (5,), edgecolor="red")