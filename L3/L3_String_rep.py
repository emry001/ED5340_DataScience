#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:53:24 2020

@author: ramanathanmuthuganapathy
"""
#String representation

#single, double and triple quote
a = 'Ramanathan'
b = "Ramanathan"
c = '''Ramanathan'''
d = """Ramanathan"""
print(a, b, c, d)

#To use characters like ', use \
msg = 'I\'m learning Python now'
print(msg)

#Raw string
rawstr = r"I\'m learning Python now"

rawstr1 = r'"Ram'
print(rawstr, '\n', rawstr1)

#multi-line strings
multi1 = '''I am learning 
Python now'''
print(multi1)

multi2 = """I am learning 
Python now"""
print(multi2)

#multi line cannot be done with double quotes
#multi3 = "I am leaning
#python"