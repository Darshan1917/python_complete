# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:09:12 2018

@author: dumapath
"""

from tkinter import *

root = Tk()

def doonclick():
    print("you are added successfully")
    
    
label1 = Label(root,text="Enter firstname")
label2 = Label(root,text="Enter lastname")
entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
    
button1 = Button(root,text="submit",fg="Blue",command=doonclick)
button1.grid(row=2,column=0)

root.mainloop()