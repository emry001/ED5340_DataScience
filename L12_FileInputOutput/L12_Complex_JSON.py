#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 22:46:31 2021

@author: ramanathanmuthuganapathy
"""


#Complex class to JSON format

import json

class Complex:
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imag = i
        
    def printdata(self):
        print(self.real, self.imag)
        
def encode_complex(x):
    if isinstance(x, Complex):
        return (x.real, x.imag)
    else:
        return TypeError('Complex object is not JSON serializable')
    
def decode_complex(dct):
    if '__Complex__' in dct:
        return Complex(dct['real'], dct['imag'])
    return dct

c = Complex(1.2, 3.3)
f = open('userdata.json', 'w+')
json.dump(c,f, default = encode_complex)
f.seek(0)
inc = json.load(f, object_hook=decode_complex)
print(inc)