# -*- coding: utf-8 -*-
"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only)

    It contains at least one letter that appears twice in a row.

    It does not contain the strings ab, cd, pq, or xy, even if they are
    part of one of the other requirements.


Created on Tue Dec 27 03:09:18 2022

@author: FAKENAME
"""

import re

def is_nice(name: str) -> bool:
    """
    Is a name nice? The name should have at least three vowels at least one
    letter twice and doesn't contain ab, cd, pq, xy.
    """

    bad_str = ["ab", "cd", "pq", "xy"]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Check for the presence of bad strings
    if [x for x in bad_str if x in name]:
        return False

    # Check that the name has at least 2 vowels
    if len([x for x in name if x in "aeiou"]) < 3:
        return False

    # Check that the name has at least one letter twice
    if not [x for x in alphabet if 2*x in name]:
        return False
    else:
        return True


def is_nice2(name: str) -> bool:
    """
    It contains a pair of any two letters that appears at least
    twice in the string without overlapping, like xyxy (xy)
    or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).

    It contains at least one letter which repeats with exactly one
    letter between them, like xyx, abcdefeghi (efe), or even aaa.
    """

    # Get pairs of chars in the name
    str_pairs = [name[i] + name[i+1] for i in range(len(name)-1)]

    # Detect char pairs that appear twice
    for pair in str_pairs:

        # Remove the first instance of the char pair
        temp_str = name.replace(pair, "", 1)

        # Test if the pair is still in the string after removal
        if pair in temp_str:
            break

    # If none of the pairs apear twice the name is not nice
    else:
        return False

    # Get a list of the chars in the name
    chars_in_name = list(set(name))

    # See if the second pattern appears in the string
    for char in chars_in_name:

        patterns = re.search(char + "[a-z]" + char, name)

        # Does the string char \w char exist in the string
        if patterns:
            return True
    else:
        return False


data = open("input.txt").read().splitlines()

nn_list = [is_nice(x) for x in data]
nn_list2 = [is_nice2(x) for x in data]

# Part 1
print(sum(nn_list))

# Part 2
print(sum(nn_list2))
