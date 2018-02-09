# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 00:04:42 2018

@author: dumapath
"""

from tkinter import *

root = Tk()

frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack(side=BOTTOM)

button1 = Button(frame1,text="SUBMIT",fg="Blue")
button2 = Button(frame2,text="clear",fg="Red")
button1.pack()
button2.pack()
root.mainloop()


