# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:13:27 2018

@author: dumapath
"""

# class creates a blue print of the instance 

class Employee:
    
    raise_amount = 1.10 # class variable 
    
    def __init__(self,fname,lname,pay): # if we have a raise amount here they are passed by subclass they can override the raise amount of this class
        self.fname = fname
        self.lname = lname
        self.email = fname+lname+"@gmail.com"
        self.pay = pay
        
    def fullname(self):
        return "Hello! {} {}".format(self.fname,self.lname)
    
    def rasiseforyear(self):
        self.pay = int(self.raise_amount*self.pay)
        
        
        
#emp1 = Employee("darshan",'umapathi',25000,2.5)# adding raise_amount here only
emp1 = Employee("darshan",'umapathi',25000)        
emp2 = Employee("farid",'khan',30000)

print (emp1.fullname())
#print(emp2.fullname())
print(emp1.pay)
emp1.rasiseforyear()  
print(emp1.pay)
a= [0, 1, 2, 3, 4]
del a[0:3:2]
print (a)
