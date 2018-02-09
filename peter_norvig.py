# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:28:30 2018

@author: dumapath
"""

# peter norvigs 

def cross(A,B):
    return [a+b for a in A for b in B]


digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

square= cross(rows,digits)
#print(square)

row_unit = [cross(row , cols) for row in rows]
#print(row_unit[1])
col_unit =[cross(rows,col) for col in cols ]
#print(col_unit[2])
box_unit = [cross(rs,cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
#print(box_unit[0])
total_unit = row_unit+col_unit+box_unit
#print(total_unit[15])
units = dict((s,[u for u in total_unit if s in u])for s in square)
print(units['C2'])
peer =  dict((s, set(sum(units[s],[]))-set([s]))for s in square)
#print (peer['C2'])
