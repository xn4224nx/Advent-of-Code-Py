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

    def find_lowest_risk_path(self):
        """
        Find the path with the lowest risk score between `start` and `end` using
        Dijkstra's algorithm. Use the algorithm listed here:
        https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        """

        # Mark all points as unvisited
        unvisited_points = set()

        # Set a tentative distance for all points as sys.maxsize apart from
        # start which is set as zero
        pnt_dist = {}

    def find_connected_points(
            self, x_coord: int, y_coord: int) -> list[(int, int)]:
        """
        For a particular point return a list of the connected points.
        """
        pass

    def calc_path_risk(self, path_points: list[(int, int)]) -> int:
        """
        Calculate the risk score of one single path defined by a list of tuple
        integers.
        """
        pass


cavern = ChitonCave("./data/sample.txt")
