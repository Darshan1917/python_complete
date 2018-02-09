# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:45:52 2018

@author: dumapath
"""

# Self adjusting widgets 
import tkinter as tk

root = tk.Tk()
label1 = tk.Label(root,text ="First", bg="Red", fg="Blue")
label1.pack(fill = X)  # this increses the width of the label samll x doesnt work
label2 = tk.Label(root,text ="Second", bg="Green", fg="Orange")
label2.pack(side = LEFT,fill = Y)

root.mainloop()