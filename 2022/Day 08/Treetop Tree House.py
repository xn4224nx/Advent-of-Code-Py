# -*- coding: utf-8 -*-
"""

--- Day 8: Treetop Tree House ---

Created on Thu Dec  8 18:09:10 2022

@author: FAKENAME

Consider your map; how many trees are visible from outside the grid?

"""

import numpy as np

# Load the Data into an a np matrix
matr = np.array([list(f) for f in open("input.txt", "r")
                    .read().splitlines()], dtype=int)

tree_count = 0
max_score = 0

# Loop over the element of the matrix
for i in range(matr.shape[0]):
    for j in range(matr.shape[1]):

        # Extract the tree size
        tree = matr[i, j]

        # # if it is on the edge it can be seen
        if i == 0 or i == matr.shape[0]-1 or j == 0 or j == matr.shape[1]-1:
            tree_count += 1
            continue

        # look at the column of trees and find the largest tree
        l_tree = matr[i, :j]
        r_tree = matr[i, j+1:]
        u_tree = matr[:i, j]
        d_tree = matr[i+1:, j]

        # If there is a tree bigger than the current one on every side this
        # Tree cannot be seen
        if np.max(l_tree) < tree or np.max(r_tree) < tree or np.max(u_tree) \
                < tree or np.max(d_tree) < tree:
            tree_count += 1

        score = 1

        # Find out how many trees can be seen in each of the arrays
        r_mask = r_tree >= tree
        d_mask = d_tree >= tree
        l_mask = np.flip(l_tree) >= tree
        u_mask = np.flip(u_tree) >= tree

        # Create the score by counting the trees till the tallest or all of
        # them if this tree is the tallest out of the array.
        if True in r_mask:
            score *= (np.argmax(r_tree >= tree) + 1)
        else:
            score *= len(r_mask)

        if True in d_mask:
            score *= (np.argmax(d_tree >= tree) + 1)
        else:
            score *= len(d_mask)

        if True in l_mask:
            score *= (np.argmax(np.flip(l_tree) >= tree) + 1)
        else:
            score *= len(l_mask)

        if True in u_mask:
            score *= (np.argmax(np.flip(u_tree) >= tree) + 1)
        else:
            score *= len(u_mask)

        if score > max_score:
            max_score = score

print(f"The number of visible trees is {tree_count}")
print(f"The max scor is {max_score}")
