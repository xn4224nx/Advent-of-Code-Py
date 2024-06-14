# -*- coding: utf-8 -*-
"""

--- Day 4: Camp Cleanup ---

In how many assignment pairs does one range fully contain the other?


Created on Sun Dec  4 14:17:52 2022

@author: FAKENAME
"""

import re


# Read the file into memory
elf_pairs = [line.rstrip() for line in open("input.txt")]

# Regex pattern of the elf pairs
elf_re = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

# Count of overlapping elves
overlap_cnt = 0
part_overlap_cnt = 0

for pair in elf_pairs:

    # Parse the number pairs
    result = elf_re.search(pair)

    elf_1_low = int(result.group(1))
    elf_1_high = int(result.group(2))

    elf_2_low = int(result.group(3))
    elf_2_high = int(result.group(4))

    # Work out if one range fully contains the other

    # Check if elf_1 is fully inside elf_2
    if elf_1_low >= elf_2_low and elf_1_high <= elf_2_high:
        overlap_cnt += 1

    # Check if elf_1 is fully inside elf_2
    elif elf_2_low >= elf_1_low and elf_2_high <= elf_1_high:
        overlap_cnt += 1

    # Work out how many partially overlap

    if elf_1_low <= elf_2_low and elf_1_high >= elf_2_low:
        part_overlap_cnt += 1

    elif elf_2_low <= elf_1_low and elf_2_high >= elf_1_low:
        part_overlap_cnt += 1

print(f"The number of overlapping pairs is {overlap_cnt}.")
print(f"The number of partially overlapping pairs is {part_overlap_cnt}.")
