"""
--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order.
Unfortunately, their accounting software uses a peculiar storage format.
That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]),
objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply
find all the numbers throughout the document and add them together.
"""

import re
import json

# Load the data from file
data = open("data/input.txt").read().splitlines()

# Extract every number in the data string
re_numbers = r"\d+|-\d+"
numbers = re.findall(re_numbers, data[0])

# Convert them to numbers and sum them
sum_of_num = sum([int(x) for x in numbers])

# Part 1 answer
print(sum_of_num)

# Parse the string into a Json
elves_json = json.loads(data[0])

# Iterate over the json Levels
