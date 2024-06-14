"""
--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say. They take turns
making sequences by reading aloud the previous sequence and using that
reading as the next sequence. For example, 211 is read as "one two,
two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value
as input for the next step. For each step, take the previous value, and
replace each run of digits (like 111) with the number of digits (3)
followed by the digit itself (1).

Starting with the digits in your puzzle input, apply this process 40 times.
What is the length of the result?

Your puzzle input is 1113222113.
"""

import itertools


def look_n_say(num_str) -> str:
    """Look and say a string of numbers"""

    new_str = []

    # for the string spilt it into groups of the same string
    split_str = ["".join(g) for k, g in itertools.groupby(num_str)]

    # For each group of the same number change into two digits,first the length
    # and secondly the number the original string is made of.
    for sub_str in split_str:
        new_str.append(str(len(sub_str)) + str(sub_str[0]))

    # Combine the array to make a new string
    ret_str = "".join(new_str)

    return ret_str


test_str_1 = "1113222113"

for i in range(50):
    test_str_1 = look_n_say(test_str_1)

# Part 1
print(f"{len(test_str_1)}")