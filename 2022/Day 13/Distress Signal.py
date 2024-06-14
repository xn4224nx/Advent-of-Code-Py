# -*- coding: utf-8 -*-
"""
--- Day 13: Distress Signal ---

Determine which pairs of packets are already in the right order.
What is the sum of the indices of those pairs?

When comparing two values, the first value is called left and the
second value is called right. Then:

    If both values are integers, the lower integer should come first.
    If the left integer is lower than the right integer, the inputs are
    in the right order. If the left integer is higher than the right integer,
    the inputs are not in the right order. Otherwise, the inputs are
    the same integer; continue checking the next part of the input.


    If both values are lists, compare the first value of each list, then the
    second value, and so on. If the left list runs out of items first,
    the inputs are in the right order. If the right list runs out of items
    first, the inputs are not in the right order. If the lists are the same
    length and no comparison makes a decision about the order, continue
    checking the next part of the input.

    If exactly one value is an integer, convert the integer to a list
    which contains that integer as its only value, then retry the comparison.
    For example, if comparing [0,0,0] and 2, convert the right value to [2]
    (a list containing 2); the result is then found by instead
    comparing [0,0,0] and [2].

Created on Sun Dec 25 23:30:30 2022

@author: FAKENAME
"""

# Load the raw signal data
raw_signal = open("sample.txt", "r").read().splitlines()

# Parse a line of signal
parsed_signal = []

sig = "[[[3,[0,7,4,6,7],[],8,[8,5,6,10]],[],2,[7],[[]]],[],[[[3,9,2,2],[8,1,1,7,4],[10,1,0]],[8],5,8],[5,3],[5,2,[[],[3,2,1,4]]]]"

# Detect the position of `[` and `]` in the signal string
left_idx = [i for i, char in enumerate(sig) if char == '[']
right_idx = [i for i, char in enumerate(sig) if char == ']']

# Extract the substrings
for i in range(len(left_idx)):
    parsed_signal.append(sig[left_idx[i]: right_idx[-i-1]+1])

new = [parsed_signal[-1]]

# Go throught the list in reverse order removing the sub strings
for i in range(len(parsed_signal)-1, 0, -1):
    new.append(parsed_signal[i-1].replace(parsed_signal[i], " "))

# Remove `[` and `]` from all the strings and split by `,`
new = [i.replace('[', '').replace(']', '').split(',') for i in new]
