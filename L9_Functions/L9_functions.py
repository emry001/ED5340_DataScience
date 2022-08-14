#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:09:41 2020

@author: ramanathanmuthuganapathy
"""


#To demonstrate functions

#Simple function with one return

#Three arguments a, b, c
def cal_sum(a, b, c):
    return (a+b+c)

#Calling the function
a1, b1, c1 = 3, 4, 5
cs = cal_sum(a1, b1, c1) # Calling the function, and getting the results in the name `cs'
print()
print('Sum of the three numbers is = ', cs)

#Positional arguments - needs to be passed in the correct order
def pos_fun(i, f, st):
    su1 = i+f
    st1 = st.upper()
    return su1, st1

i1, f1, st1 = 5, 6.34, 'Ram'
out1, out2 = pos_fun(i1, f1, st1)
print('Function returning multiple values ', out1, out2)

out_lst = pos_fun(f1, i1, st1)
print('Function returning multiple values as a tuple', out_lst, type(out_lst))

# i1, st1, f1 = 5, 6.34, 'Ram' #Changing the arguments 
# out_lst1 = pos_fun(i1, f1, st1) # Not working as expected

# i1, st1, f1 = 5, 'Ram', 6.34 #Changing the arguments 
# out_lst1 = pos_fun(i1, st1, f1) # Not working as expected

#Keyword arguments
out_lst2 = pos_fun(i=10, f=20.3, st='Ram')
print('Using keyword arguments', out_lst2)
out_lst3 = pos_fun(i=10, st='Ram', f=20.3)
print('Changing the order for keyword arguments', out_lst3)

print()
print('For the keyword arguments to work, same name is needed for arguments in both function and passing')

#Using comb. of postional and keyword arguments

def pos_kw(i, j, k):
    su1 = i+j
    st1 = k.upper()
    return su1, st1

out1, out2 = pos_kw(10, j = 23.67, k = 'Ram')
print(out1, out2)

print()
print('uncomment the following to do the demo')
# out1, out2 = pos_kw(i = 10, 23.67, k = 'Ram')
# print(out1, out2)


