"""
--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well. Not
everyone gets along! This year, you resolve, will be different. You're going to
find the optimal seating arrangement and avoid all those awkward conversations.
"""

import re
import random
from itertools import permutations


def table_happiness(people_at_table, pref_dict):
    """Calculate the happiness of the current table setup."""
    happiness_sum = 0

    # Iterate over people and calculate the happiness
    for i in range(len(people_at_table)):

        # Catch person at the start of the list
        if i == 0:
            prev_i = len(people_at_table) - 1
        else:
            prev_i = i - 1

        # Catch a person at the end of the list
        if i == len(people_at_table) - 1:
            next_i = 0
        else:
            next_i = i + 1

        # Calculate the happiness caused by the prev person
        if people_at_table[prev_i] in pref_dict[people_at_table[i]]:
            happiness_sum += pref_dict[people_at_table[i]][
                people_at_table[prev_i]]

        # Calculate the happiness caused by the next person
        if people_at_table[next_i] in pref_dict[people_at_table[i]]:
            happiness_sum += pref_dict[people_at_table[i]][
                people_at_table[next_i]]

    return happiness_sum


# Load the data from file
data = open("data/input.txt").read().splitlines()

# Parse the preference data into a structured format
pref_re = r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)"

pref_data = {}

# Iterate over the lines of the data
for line in data:

    # Extract the key parts of the data
    line_tup = re.findall(pref_re, line)[0]

    # Add in the person if they are missing
    if line_tup[0] not in pref_data:
        pref_data[line_tup[0]] = {}

    # Get the change in the right format
    if line_tup[1] == "gain":
        change = int(line_tup[2])

    elif line_tup[1] == "lose":
        change = -1 * int(line_tup[2])

    # Add in the preference data
    pref_data[line_tup[0]][line_tup[3]] = change

# Add in yourself
pref_data["Me"] = {}

# People to be seated
people = list(pref_data.keys())

# Get the possible permutations of the people at the table and calculate the
# happiness.
happy_results = []
for table_perm in permutations(people):
    happy_results.append(table_happiness(list(table_perm), pref_data))

print(max(happy_results))
