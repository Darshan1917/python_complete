# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:20:42 2018

@author: dumapath
"""

class Employee:
    
    raise_amount = 1.10 # class variable 
    
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.email = fname+lname+"@gmail.com"
        self.pay = pay
        
    def fullname(self):
        return "Hello! {} {}".format(self.fname,self.lname)
    
    def rasiseforyear(self):
        self.pay = int(self.raise_amount*self.pay)
        

# now we have created a employee class but there are different types of employee like programmer and manager 
# they hev extra features to be involved like programmer have which all language he knows and 
        # manager who are below him 
        
        
# create a class called programmer 
class Programmer(Employee):
    pass
# it goes here and searches for the init method but doesnt get any hence goes and searches in 
    # the inhereted class finds it and execute it 


dev = Programmer("mary",'jane',2100)
print (dev.email)
    
