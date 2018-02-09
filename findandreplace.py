# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 19:25:23 2018

@author: dumapath
"""

# find and replaee using Regular expression

import re 

# house number are AS3 DE3

house = input("enter a house number")
pattern = re.compile(r'[A-Z]{2}[0-9]')
if re.match(pattern,house):
    print ("Corrct house")
else:
    print ("Wrong house")
