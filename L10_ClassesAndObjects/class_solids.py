#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:46:12 2020

@author: raman
"""
import math

class Solid:
    def __init__(self, case):
        self.case = case
        
    def compute_sa_vol(self):
        if self.case == 0:
            a = float(input('Enter the side of a cube: ' ))
            sa = 6*a*a
            vol = a**3
            
        elif self.case == 1:
            r,h = input('Enter rad and height of a cylinder ').split()
            rad = float(r)
            ht = float(h)
            sa = 2* math.pi * rad * ht
            vol = math.pi * rad ** 2 * ht
        else:
            r = float(input('Enter radius of a sphere ' ))
            sa =  math.pi * r ** 2
            vol = math.pi * r ** 3
        
        return sa, vol
    
    def __del__(self):
        print('Deleting the object '+ str(self))
    
cube = Solid(0)
sa, vol = cube.compute_sa_vol()
print(sa, vol)
cyl = Solid(1)
sa, vol = cyl.compute_sa_vol()
print(sa, vol)
sph = Solid(3)
sa, vol = sph.compute_sa_vol()
print(sa, vol)