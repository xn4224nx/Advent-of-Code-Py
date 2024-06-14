# -*- coding: utf-8 -*-
"""

--- Day 3: Perfectly Spherical Houses in a Vacuum ---

How many houses receive at least one present?

Created on Mon Dec 26 22:07:28 2022

@author: FAKENAME
"""

# Load the data
data = open("input.txt", 'r').read()

santa_loc = (0, 0)
rob_loc = (0, 0)
visited = {santa_loc: 1}

# Loop over the data and move according to commands
for i in range(len(data)):

    com = data[i]

    if i % 2 == 0:

        # Move Santa
        if com == '^':
            santa_loc = (santa_loc[0], santa_loc[1]+1)

        elif com == 'v':
            santa_loc = (santa_loc[0], santa_loc[1]-1)

        elif com == '<':
            santa_loc = (santa_loc[0]-1, santa_loc[1])

        elif com == '>':
            santa_loc = (santa_loc[0]+1, santa_loc[1])

        # Updated the visited dict
        if santa_loc in visited:
            visited[santa_loc] += 1
        else:
            visited[santa_loc] = 1

    else:
        # Move Robo-Santa
        if com == '^':
            rob_loc = (rob_loc[0], rob_loc[1]+1)

        elif com == 'v':
            rob_loc = (rob_loc[0], rob_loc[1]-1)

        elif com == '<':
            rob_loc = (rob_loc[0]-1, rob_loc[1])

        elif com == '>':
            rob_loc = (rob_loc[0]+1, rob_loc[1])

        if rob_loc in visited:
            visited[rob_loc] += 1
        else:
            visited[rob_loc] = 1

# Part 2
print(len(visited))
