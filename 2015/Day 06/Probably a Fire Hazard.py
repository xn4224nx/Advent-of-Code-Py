# -*- coding: utf-8 -*-
"""

--- Day 6: Probably a Fire Hazard ---

After following the instructions, how many lights are lit?

Created on Fri Dec 30 11:38:21 2022

@author: FAKENAME
"""
import re
import numpy as np

# Load the instructions data
data = open("input.txt").read().splitlines()

# Split the instruction data
re_pat = r"(\D+) (\d+),(\d+) (\D+) (\d+),(\d+)"
data = [re.findall(re_pat, x)[0] for x in data]

# Define the np array to store the light data
lights = np.zeros((1000, 1000), dtype=bool)
lights2 = np.zeros((1000, 1000), dtype=int)

# Process the instructions and turn the lights on or off
for instruct in data:

    # Parse the coordinate data into variables
    x1 = int(instruct[1])
    y1 = int(instruct[2])
    x2 = int(instruct[4])+1
    y2 = int(instruct[5])+1

    # Act on the instructions
    if instruct[0] == "toggle":

        # Part 1
        lights[x1:x2, y1:y2] = np.invert(lights[x1:x2, y1:y2])

        # Part 2
        lights2[x1:x2, y1:y2] += 2

    elif instruct[0] == "turn on":

        # Part 1
        lights[x1:x2, y1:y2] = True

        # Part 2
        lights2[x1:x2, y1:y2] += 1

    elif instruct[0] == "turn off":

        # Part 1
        lights[x1:x2, y1:y2] = False

        # Part 2
        lights2[x1:x2, y1:y2] -= 1

    # Ensure no lights brightness goes lower than zero
    lights2 = np.where(lights2 > 0, lights2, 0)


# Part 1 Answer
print(f"The number of lights on is {np.sum(lights)}.")


# Part 2 Answer
print(f"The number of lights on is {np.sum(lights2)}.")
