# -*- coding: utf-8 -*-
"""

--- Day 1: Not Quite Lisp ---

Created on Mon Dec 26 21:11:32 2022

@author: FAKENAME
"""

data = open("input.txt", 'r').read()

left = data.count('(')
right = data.count(')')

print(left-right)

floor = 0

for i in range(len(data)):

    if data[i] == '(':
        floor += 1

    elif data[i] == ')':
        floor -= 1

    if floor < 0:
        print(i+1)
        break
