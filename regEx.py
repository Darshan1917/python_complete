# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Trying out basic of regular expression

import re
Nameage = "Jane is 22 and Mark is 53 and Raj is 16"
age = re.findall(r'\d{1,3}',Nameage)
print(age)
name = re.findall(r'[A-Z][a-z]*',Nameage)
print (name)



Text_to_speech = '''abcdefghijklmnopqrstuvwxyz
                    ABCDEFGHIJKLMNOPQRSTUVWXYZ
                    ABCDEFG
                    
                    haha ha ha 
                    Joker 
                    
                    789-996-987-987
                    369.258.741.555
                    258.741.555
                    
                    
                    Mr.Trump
                    Mr.Modi
                    Farid , Arvind, 
                    Sathi_Skrishnam@gmail.com
                    mall.im@gmail.com'''
                    
# In complie we will write the pattern that has to be matched 
# Now compre that with the string we have 
# We use finditer method to find all the iterations and also span (where it is to be found in the string ) 
pattern =  re.compile(r'ABC')
match = pattern.finditer(Text_to_speech)
for mat in match:
    print (mat)
# see the result <_sre.SRE_Match object; span=(48, 51), match='ABC'> and <_sre.SRE_Match object; span=(95, 98), match='ABC'>
    
# NOTE that the dot opertor (.) includes everything it is like a universal charater 
# when we run the code then we will see how it works 
    # UNcomment the below code and check the output
"""pattern =  re.compile(r'.')
match = pattern.finditer(Text_to_speech)
for mat in match:
    print (mat)"""
    
# so how can we use them the dot explicitly we can run them by using "\" sign before them
# NOw only the dots have been captured    (used in email matching) 
pattern =  re.compile(r'\.')
match = pattern.finditer(Text_to_speech)
for mat in match:
    print (mat)
    
# Lets see if we can get a email from the big list  *or+   
    
pattern =  re.compile(r'[A-Z][A-Za-z\.\_]*@gmail.com')
match = pattern.finditer(Text_to_speech)
for mat in match:
    print (mat)
 
# prints all the blanks
# uncomment anc check the output 
'''pattern =  re.compile(r' ')
match = pattern.finditer(Text_to_speech)
for mat in match:
    print (mat)'''
    
 # we are matching the phone number given    
pattern =  re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d[-.]\d\d\d')
match = pattern.finditer(Text_to_speech)
for mat in match:
    print (mat)

# instead of doing this we can use \d+ select all the digits or \d{1,3} ie \d{min,max}
# NOTE NOTE here we need to know thw exact length else it will not give any error but not throw any error
pattern =  re.compile(r'\d+\.\d{3}\.\d+')
match = pattern.finditer(Text_to_speech)
for mat in match:
    print (mat)
    
# note the   re.compile(r'\d{1,9}') is the range not the digits matching 
# try : re.compile(r'\d{1}') , re.compile(r'\d{6}') , re.compile(r'\d{2}') 
pattern =  re.compile(r'\d{2}')
match = pattern.finditer(Text_to_speech)
for mat in match:
    print (mat)
    
    
FNames = ''' Mr. Schafer
             Mr Smith
             Mrs Robinson
             Ms Davis
             Mr.T'''
             
#pattern = re.compile(r'[A-Z][a-zA-Z. ]*')
#match = pattern.finditer(FNames)
#for mat in match:
#    print (mat)

pattern = re.compile(r'(Mr|Ms|Mrs)')
match = pattern.finditer(FNames)
for mat in match:
    print (mat)     
    

    
    









