# -*- coding: utf-8 -*-
"""

--- Day 5: Supply Stacks ---

After the rearrangement procedure completes, what crate ends
 up on top of each stack?

Created on Mon Dec  5 18:45:27 2022

@author: FAKENAME
"""

import re

raw_crates = []
raw_instructions = []
crates = True

# Load the data into memory
with open("input.txt") as file:

    for line in file:

        line = line.rstrip('\n')

        # Work out where the split between tha data parts is
        if line == "":
            crates = False
            continue

        # Save the raw data
        if crates:
            # Extract the initial crate setup
            raw_crates.append(line)
        else:
            # Extract the instructions
            raw_instructions.append(line)

# Detect the number of columns in the problem
crate_col_idx = [int(f.strip()) for f in raw_crates[-1].split()]

# Create a dict to store the crate stacks
crate_dict = {idx: [] for idx in crate_col_idx}

# Regex to extract the crates
crate_re = re.compile(r"\[[A-Z]\]")

# Fill the crate dict from the raw_instructions
for row_idx in range(len(raw_crates)-2, -1, -1):

    row_str = raw_crates[row_idx]

    for crate in crate_re.finditer(row_str):

        # What column is the crate in
        crate_col = 1 + crate.start()//4

        # What is the single letter name
        crate_name = crate.group()[1]

        # Add it into the `crate_dict`
        crate_dict[crate_col].append(crate_name)

# Parse the instructions
instruc_re = re.compile(r"\d+")
instruc = [list(map(int,
                    instruc_re.findall(line))) for line in raw_instructions]

# Implement the instructions
# command[0] = Number to move
# command[1] = Exodus Column
# command[2] = Destination Column

for command in instruc:

    # How many are moving
    for mov in range(command[0]):

        # Add the create to the end of the detination column and remove
        # from the exodus column with pop

        # Part 1
        # crate_dict[command[2]].append(crate_dict[command[1]].pop())
        pass

    # Part 2

    # Work out the crates that are going to be moved
    crates_2_mov = crate_dict[command[1]][-1 * command[0]:]

    # Remove the crates from the exodus col
    crate_dict[command[1]] = crate_dict[command[1]][: -1 * command[0]]

    # Add the crates onto the detisnation col
    crate_dict[command[2]] += crates_2_mov


# Find out what is crate is on the top of each pile
ret_str = ""

for col in crate_dict:

    if crate_dict[col]:
        ret_str += crate_dict[col][-1]












# Parse the instructions

# Run the simulation of the instructions of the inital crate setup

# Extract the top layer of the crate stack
