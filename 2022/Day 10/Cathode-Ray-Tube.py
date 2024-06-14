# -*- coding: utf-8 -*-
"""

--- Day 10: Cathode-Ray Tube ---

Part 1:

    Find the signal strength during the 20th,
    60th, 100th, 140th, 180th, and 220th cycles.
    What is the sum of these six signal strengths?

Created on Thu Dec 22 23:37:44 2022

@author: FAKENAME
"""

# Load Instructions
instrucs = open("input.txt", "r").read().splitlines()

# Simulate the CPU cycle
cpu_reg = {}

# The count of the cycle and the current register value
x_reg = 1
cycle = 1

for ins in instrucs:

    if ins == "noop":

        # Save the value of the register
        [cpu_reg.update({i: x_reg}) for i in range(cycle, cycle+1)]

        # Increment the cycle
        cycle += 1

    # Deal with the addx command
    else:

        # Extract the value of the addx command
        add_v = int(ins.split()[1])

        # Save the value of the register
        [cpu_reg.update({i: x_reg}) for i in range(cycle, cycle+2)]

        # Increment the register
        x_reg += add_v

        # Increment the cycle
        cycle += 2


# What is the sum of the signal strength at the 20th, 60th,
# 100th, 140th, 180th, and 220th cycles

sum = 0

for i in [20, 60, 100, 140, 180, 220]:

    sum += (i * cpu_reg[i])

print(f"The sum of the cycles is {sum}.")

# Part 2 - What Letters are displayed

# Loop over the `cpu_reg` and calculate for each cycle if a pixel was showing
for cycle, reg_x in cpu_reg.items():

    # Calculate line position of the sprite from cycle
    l_pos = (cycle % 40)-1

    # If register is close to the value of the cycle
    if reg_x > l_pos-2 and reg_x < l_pos+2:

        # Print a full pixel
        print('#', end='')

    else:

        # Print an empty pixel
        print(' ', end='')

    # Print a new line
    if cycle % 40 == 0:
        print()
