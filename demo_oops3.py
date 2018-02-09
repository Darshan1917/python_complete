# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:33:26 2018

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
 # adding new attributes in the subclass along with thr parent class
class Programmer(Employee):
    
    def __init__(self,fname,lname,pay,programming_lang=None):
        super().__init__(fname,lname,pay)
#        self.programming_lang =programming_lang
        if programming_lang is None:
            self.programming_lang=[]
        else:
            self.programming_lang=programming_lang
            
    def add_prog(self,program):
        if program not in self.programming_lang:
            self.programming_lang.extend(program)
            
    def remove_prog(self,program):
        for n in program:
            print(n)
            if n in self.programming_lang:
                self.programming_lang.remove(n)


dev1 = Programmer("a","m",2500)
print (dev1.pay)
print (dev1.programming_lang)
dev1.add_prog(["javascript","ML","J2EE","Java"])
print (dev1.programming_lang)
dev1.remove_prog(["ML","Java"])
print (dev1.programming_lang)


