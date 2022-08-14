#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:22:15 2020

@author: ramanathanmuthuganapathy
"""

# To demonstrate Loops - while and for

str1 = "Raman"
for ele in str1:
    print(ele)

# The following won't work - uncomment them during demo
str1 = "Raman"
while ele in str1:
    print(ele)
    
#You can do the following - C style printing
i = 0
while i < len(str1):
    print(i, str1[i])
    i += 1

#How do you do the above with for loop
    
i = 0
while i < 10:
    i += 1;
    print(i)

# The following won't work - uncomment them during demo
# i = 0
# for i < 10:
#     i = i + 1;
#     print(i)
    
#What is the equivalent for st for the while. Use range()
for i in range(0,10,1):
    i = 20
    print(i)

#You can simply the above as follows
for i in range(10):
    print(i)
    
for i in range(10,2,-2):
    print(i)



 
# Uncomment during the demo
# for i in range(0, len(str1)):
#     print(i, str1[i])

#Another way
# for i, ele in enumerate(str1):
#     print(i, str1[i])
    
print(-3%2)
num = int(input('Enter an input: '))
while num < 100:
    if num < 0:
        print('number is negative')
        pass
    elif num % 2 == 0:
        print('num is even')
    else:
        print('number is odd')
        break
    num = int(input('Enter an input: '))
else:
    print('The number is not less than 100')

# for i,j in range(0,5):
#     print(i,j)
#nested for loop
for i in range(5):
    for j in range(5):
        print(i+j)
        
for i in range(5):
    j = 0
    while j < 5:
        print(i+j)
        j += 1
        
for i in range(0,10,1):
    i = 20
    print(i)

i = 0
for i in range(0,10,1):
    print(i)
    
i = 0
s = 0
while i < 5:
    s += i
    i+=1
print(s)

