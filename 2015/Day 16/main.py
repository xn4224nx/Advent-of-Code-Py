"""
--- Day 16: Aunt Sue ---

So, to avoid sending the card to the wrong person, you need to figure out which
Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the
gift. You open the present and, as luck would have it, good ol' Aunt Sue got
you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed,
as the case may be.

What is the number of the Sue that got you the gift?
"""

import re

main_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

# Import the data
data = open("data/input.txt").read().splitlines()

# Parse the data
sue_info_re = r"(\w+): (\d+),?\s*"
sune_name_re = r"Sue (\d+)"

data = {int(re.findall(sune_name_re, x)[0]
            ): re.findall(sue_info_re, x) for x in data}

# Put the data into a dictionary
new_data = {}

for sue, info in data.items():
    temp = {}

    for i in info:
        temp[i[0]] = int(i[1])

    new_data[sue] = temp

results = {}

# For each aunt check how they compare to the main sue
for sue, info in new_data.items():

    score = 0

    # Iterate over every characteristic in dictionary
    for char, val in info.items():

        # If the characteristic is in main dict, check the value matches
        if char in main_sue:

            if char in ["cats", "trees"] and val > main_sue[char]:
                score += 1

            elif char in ["pomeranians", "goldfish"] and val < main_sue[char]:
                score += 1

            elif val == main_sue[char]:
                score += 1

    results[sue] = score

print(max(results, key = results.get))