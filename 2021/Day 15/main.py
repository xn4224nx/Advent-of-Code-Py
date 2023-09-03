"""
--- Day 15: Chiton ---

The cavern is large, but has a very low ceiling, restricting your motion to two
dimensions. The shape of the cavern resembles a square; a quick scan of chiton
density produces a map of risk level throughout the cave (your puzzle input).

You start in the top left position, your destination is the bottom right
position, and you cannot move diagonally. The number at each position is its
risk level; to determine the total risk of an entire path, add up the risk
levels of each position you enter (that is, don't count the risk level of your
starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk.

Part 1:
    What is the lowest total risk of any path from the top left to the bottom
    right?
"""

import numpy as np


class ChitonCave:

    def __init__(self, datafile: str):

        # Load the cave data from file and parse the risk map
        self.risk_map = np.array(
            [[int(x) for x in y] for y in
             open(datafile, "r").read().splitlines()])

        # Define the start and end points
        self.start = (0, 0)
        self.end = (self.risk_map.shape[0]-1, self.risk_map.shape[1]-1)


cavern = ChitonCave("./data/sample.txt")
