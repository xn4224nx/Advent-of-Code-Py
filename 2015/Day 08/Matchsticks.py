# -*- coding: utf-8 -*-
"""

--- Day 8: Matchsticks ---

Disregarding the whitespace in the file, what is the number of characters of
code for string literals minus the number of characters in memory for the
values of the strings in total for the entire file?

Created on Fri Dec 30 17:45:28 2022

@author: FAKENAME
"""

import re

str_re = r'(\\")|(\\\\)|(\\x[a-f0-9]{2})'

raw_data = open("input.txt").read().splitlines()

# The total length of the strings in memory, file and expanded
total_len_str = 0
total_len_mem = 0
total_len_exp = 0

# Iterate over each line of the file
for line in raw_data:

    # The length of the string in file
    total_len_str += len(line)

    # For the line replace the escape chars with a replacement char
    mem_line = re.sub(str_re, "0", line)

    # The length of the string in mem (remove 2 for the outside quotes)
    total_len_mem += len(mem_line)-2

    # Expand the string by replacing every " in the sting with \"
    # Change every \ to \\

    # Ignore the first and last char
    exp_line = line[1:-1]

    # Replace \ with \\
    exp_line = re.sub(r"(\\)", r"\\\\", exp_line)

    # Replace " with \"
    exp_line = re.sub(r"(\")", r"\"", exp_line)

    # Add in the outer " with escape chars
    exp_line = r'"\"' + exp_line + r'\""'

    # Total expanded length
    total_len_exp += len(exp_line)

    print(line)
    print(mem_line)
    print(exp_line)
    print()

# Part 1
print(total_len_str - total_len_mem)

# Part 2
print(total_len_exp - total_len_str)
