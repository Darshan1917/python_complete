# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:31:08 2018

@author: dumapath
"""

from tkinter import *


# this shows how class is used to create a everything on the gui 
class mybuttons:
    def __init__(self,rootone):
        frame = Frame(rootone)
        frame.pack()
        
        self.printbutton = Button(frame,text="submit",fg="Red",command=self.printmessage)
        self.printbutton.pack()
        self.exitbutton = Button(frame,text="exit",fg="Green",command=frame.quit)
        self.exitbutton.pack(side=RIGHT)
        
        
    def printmessage(self):
        print("Button clicked")
        
        

root =Tk()

b=mybuttons(root)
root.mainloop()