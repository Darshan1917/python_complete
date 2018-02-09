# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:34:56 2018

@author: dumapath
"""
def spam():
 eggs = 99
 bacon()
 print(eggs)
 
def bacon():
    ham = 101
    eggs = 0


spam()  


# global varibales can be read as local also 

def spam():
 print(eggs)
eggs = 42
spam()
print(eggs)



# same name
eggs = 'global'
def spam():
    #   eggs = 'spam local'
    print(eggs) # prints 'spam local'
def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

bacon()
print(eggs) 


def spam():
   #print(eggs) # Gives error 
   global eggs
   eggs = '@spam'
   print(eggs)
  
  
def bacon():
    eggs= "bacon"
    
    
def ham():
    print (eggs)
    
eggs = '@global'
spam()
print(eggs)
ham()
print(eggs)