"""
--- Day 3: Squares With Three Sides ---

In a valid triangle, the sum of any two sides must be larger than the remaining
side. For example, the "triangle" given above is impossible, because 5 + 10 is
not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""

import numpy as np


def is_triangle(sides) -> bool:
    """Is the side lengths a triangle"""

    # If any of the sides are greater than the sum of the others return False
    if sides[0] >= sides[1] + sides[2] or sides[1] >= sides[0] + sides[2] or \
            sides[2] >= sides[0] + sides[1]:
        return False
    else:
        return True


# Load the triangle side lengths
side_lens = open("data/input.txt").read().splitlines()
side_lens = [x.strip().split() for x in side_lens]
side_lens = [[int(x) for x in y] for y in side_lens]

# Prep the data for part 2
side_lens2 = np.array(side_lens).flatten('F')

results = []
results2 = []

# Test is each one is a possible triangle
for tri in side_lens:
    results.append(is_triangle(tri))

# Part 1
print(sum(results))

for i in range(0, len(side_lens2), 3):

    tri2 = list([side_lens2[i], side_lens2[i+1], side_lens2[i+2]])

    results2.append(is_triangle(tri2))

# Part 2
print(sum(results2))
