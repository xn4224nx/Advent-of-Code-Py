"""
--- Day 6: Signals and Noise ---

All you need to do is figure out which character is most frequent for each
column.

Given the recording in your puzzle input, what is the error-corrected version
of the message being sent?
"""

import numpy as np
from collections import Counter

# Load the data into a numpy grid
data = open("data/input.txt").read().splitlines()
data = np.array([[y for y in x] for x in data])

# For each of the columns feed its contents into a Counter
for col in range(data.shape[1]):
    print(Counter(data[:, col]).most_common()[-1][0][0], end="")
