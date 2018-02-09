# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:44:39 2018

@author: dumapath
"""

# this is a place we have oops concepts demo 
# class creation 
import datetime

class User:
    
    #init is a constructer and must be present in the program
    def __init__(self,fname,lname,dob):
        self.fname = fname
        self.lname = lname
        self.email = fname+lname+"@gmail.com"
        self.dob = dob
        
    def fullname(self):
        return self.fname+' '+self.lname
    
#    def age(self,dob):
#        today = datetime.date.today()
#        bday = self.dob.strftime("%Y-%m-%d")
#        bday_new =bday[0:4]
#        age_in_years = int(today-bday_new)
#        return age_in_years
    
 # user1 is an instance of User and we can use the functions in User     
user1 = User("John","david",'1971-07-05')
print(user1.fullname().split(" "))
print(user1.dob)
#print(user1.age("1971-07-05"))
