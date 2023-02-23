"""
--- Day 11: Hex Ed ---

You are on an infinite hexagonal grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be
found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \



You have the path the child process took. Starting where he started, you need
to determine the fewest number of steps required to reach him. (A "step" means
to move from the hex you are in to any adjacent hex.)

"""

import math


class HexGrid:

    def __init__(self, current_path = None):

        self.current_path = current_path
        self.max_distance = 0
        self.curr_coord = [0, 0] # q r
        self.viable_directions = {
            'n': (0, -1),
            'ne': (1, -1),
            'se': (1, 0),
            's': (0, 1),
            'sw': (-1, 1),
            'nw': (-1, 0)
        }

    def load_path(self, file_path: str) -> list[str]:
        """Load the file that has the hex grid directions."""
        self.current_path = open(file_path).read().strip().split(",")

    def grid_move(self, direction: str):
        """Move along the grid in one of the six directions."""

        for i in range(len(self.curr_coord)):
            self.curr_coord[i] += self.viable_directions[direction][i]

            if self.steps_from_origin() > self.max_distance:
                self.max_distance = self.steps_from_origin()

    def steps_from_origin(self):
        """Find the shortest number of steps back to the origin."""
        return (abs(self.curr_coord[0]) +
                abs(self.curr_coord[0] + self.curr_coord[1]) +
                abs(self.curr_coord[1])) / 2

    def follow_path(self):
        """Follow path on the hex grid"""

        for direction in self.current_path:
            self.grid_move(direction)


path_0 = ["ne","ne","ne"]
path_1 = ["ne","ne","sw","sw"]
path_2 = ["ne","ne","s","s"]
path_3 = ["se","sw","se","sw","sw"]

child = HexGrid()
child.load_path("data/input.txt")

child.follow_path()

# Part 1
print(child.steps_from_origin())

# Part 2
print(child.max_distance)
