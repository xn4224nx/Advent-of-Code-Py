# -*- coding: utf-8 -*-
"""

--- Day 2: I Was Told There Would Be No Math ---

All numbers in the elves' list are in feet.
How many total square feet of wrapping paper
should they order?

Created on Mon Dec 26 21:25:55 2022

@author: FAKENAME
"""

# Load the data
data = open("input.txt", 'r').read().splitlines()

# Parse the data
data = [x.split('x') for x in data]
data = [[int(y) for y in x] for x in data]

areas = []
ribons = []

# Calculate areas
for x in data:

    # Calculate the area of wrapping papaer needed
    area = 2*x[0]*x[1] + 2*x[1]*x[2] + 2*x[2]*x[0]
    small_side_area = min([x[0]*x[1], x[1]*x[2], x[2]*x[0]])

    areas.append(area + small_side_area)

    # Calculate the length of ripon needed
    small_side_perim = min([
            x[0] + x[0] + x[1] + x[1],
            x[0] + x[0] + x[2] + x[2],
            x[1] + x[1] + x[2] + x[2],
        ])

    ribons.append(x[0]*x[1]*x[2] + small_side_perim)

# Part 1
print(sum(areas))

# Part 2
print(sum(ribons))
