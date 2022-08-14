#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:12:39 2021

@author: ramanathanmuthuganapathy
"""


#JSON demonstration - string to dict and so on 

#json object (format) looks similar to a 
#dictionary with double quotes

# In python, json exist as string 
import json

#per is a  string following JSON format

per = '{"name": "Ram", "languages": ["Python", "C++"]}'
# per = {"name": "Ram", "languages": ["Python", "C++"]}
# per = "{'name': 'Ram', 'languages': ['Python', 'C++']}"
print(per)
per_dct = json.loads(per)

print(per_dct)
print(type(per_dct))

#per_dct is a dictionary converted by json.loads

print(per_dct['name'])
print(per_dct['languages'])

#input json file is person.json (which is in json format)

with open('person.json', 'r') as f:
    data = json.load(f) #data is a dictionary 
    
print(data)
    
# Convert dict to JSON
dct = {'name': 'Ram', 'languages': ['Python', 'C++']}

print(type(dct))
string = json.dumps(dct)

print(string)

# Writing JSON to a file

dict1 = {"name": "Raman",
"languages": ["Python", "C", "C++"],
"deparment": "ED",
"working": True
}

print(dict1)

with open('outputdata.json', 'w') as fi:
    json.dump(dict1, fi) #transforms dict to JSON string
    
#Printing a JSON string with indentation

person_str = '{"name": "Ram", "languages": ["Python", "C++"]}'

# Getting dictionary
person_dict = json.loads(person_str)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))