# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:27:24 2018

@author: dumapath
"""

#login  page email verfication using regEx

import re

email = input("Enter the email id")
pattern =  re.compile(r'[A-Za-z._0-9]+[@][a-z]+[.][com|edu|net]+')
if re.match(pattern,email):
    print("correct email")
else:
    print ("enter valid email")
    
    
    
# Search 
    
pattern = re.compile(r"eggs")
value= pattern.finditer("eggs")
for val in list(value):
    print (val)
if re.search(pattern,"beconeggseggbacon"):
    print ("match found ") 
else:
    print("No match ")