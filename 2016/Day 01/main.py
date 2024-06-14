"""
--- Day 1: No Time for a Taxicab ---

The Document indicates that you should start at the given coordinates (where
you just landed) and face North. Then, follow the provided sequence: either
turn left (L) or right (R) 90 degrees, then walk forward the given number of
blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you
take a moment and work out the destination. Given that you can only walk on
the street grid of the city, how far is the shortest path to the destination?

How many blocks away is Easter Bunny HQ?
"""

import re
import itertools

# Load the input data
data = open("data/input.txt").read().split(",")

# Define the initial Conditions as complex numbers
position = 0 + 0j
direction = 0 + 1j

visited_positions = [position]

# Parse the direction and distance
data = [re.findall(r"(R|L)([0-9]+)", x)[0] for x in data]

for instruct in data:

    # Change the direction
    if instruct[0] == 'R':
        direction *= -1j
    else:
        direction *= 1j

    # Move the person
    for i in range(1, int(instruct[1])+1):
        position += direction

        if position not in visited_positions:
            visited_positions.append(position)

        else:
            # Part 2
            print(position)
            print(abs(position.real) + abs(position.imag))
# Part 1
print(abs(position.real) + abs(position.imag))
