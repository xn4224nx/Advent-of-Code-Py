# -*- coding: utf-8 -*-
"""

--- Day 3: Rucksack Reorganization ---

The list of items for each rucksack is given as characters
all on a single line. A given rucksack always has the same
number of items in each of its two compartments, so the first half
of the characters represent items in the first compartment,
while the second half of the characters represent items in the
second compartment.

The ruck sack should only have one common letter between both sides

To help prioritize item rearrangement, every item type can be
converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.


QUESTION:

    Find the item type that appears in both compartments of
    each rucksack. What is the sum of the priorities
    of those item types?

Created on Sat Dec  3 17:22:05 2022

@author: FAKENAME
"""


def char_2_priority(c):

    if c.islower():
        return ord(c) - ord('a') + 1

    elif c.isupper():
        return ord(c) - ord('A') + 27

    else:
        raise Exception(f"Invalid input {str(c)}")


def com_char_2(str_1, str_2):

    for c1 in str_1:

        if c1 in str_2:
            return c1


def com_char_3(str_1, str_2, str_3):

    for c1 in str_1:

        if c1 in str_2 and c1 in str_3:
            return c1


bag_scores = []
elf_bags = []
sec_bag_scores = []

# Read the file into memory
with open("input.txt") as file:

    # Read the line in one at a time
    for line in file:

        # remove the endline char
        line = line.rstrip()

        # Save the line into a list
        elf_bags.append(line)

# sum of the priorities Calculation
for i in range(len(elf_bags)):

    bag = elf_bags[i]

    # Split the line into two
    hal_ln_len = int(len(bag)/2)

    # Create the two bags
    compart_1 = bag[:hal_ln_len]
    compart_2 = bag[hal_ln_len:]

    assert (len(compart_1) == len(compart_2))

    # work out the commom element between the bags
    c_char = com_char_2(compart_1, compart_2)

    # calculate the score from the common element
    bag_scores.append(char_2_priority(c_char))

    # Calculate the scores from the comon element accross multiple bags
    if (i+1) % 3 == 0:

        # work out the commom element between the bags
        c2_char = com_char_3(elf_bags[i-2], elf_bags[i-1], elf_bags[i])

        # calculate the score from the common element
        sec_bag_scores.append(char_2_priority(c2_char))

    # Debugging
    # print(line)
    # print(c_char)
    # print(bag_1)
    # print(bag_2)
    # print()


print(f"Part1: The sum of the priorities is {sum(bag_scores)}")
print(f"Part2: The sum of the priorities is {sum(sec_bag_scores)}")
