"""
--- Day 13: Transparent Origami ---

The first section is a list of dots on the transparent paper. 0,0 represents the
top-left coordinate. The first value, x, increases to the right. The second
value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and
the coordinate 0,7 is below 0,0.

Then, there is a list of fold instructions. Each instruction indicates a line on
the transparent paper and wants you to fold the paper up (for horizontal y=...
lines) or left (for vertical x=... lines).

Part 1:
    How many dots are visible after completing just the first fold instruction
    on your transparent paper?
"""

import numpy as np


class TransPaper:

    def __init__(self, data_file: str):

        self.coords = []
        self.folds = []

        # Load the raw data from file and parse
        for line in open(data_file, 'r').read().splitlines():

            if ',' in line:
                self.coords.append(tuple(int(x) for x in line.split(",")))

            elif "fold along" in line:
                axis, mag = line.split('=')
                self.folds.append([axis[-1], int(mag)])

    def fold_paper(self, axis: str, pos: int):
        """
        Fold the paper along a certain line defined by `axis` and `pos`,
        recalculate the dots new position and remove duplicates.
        """
        pass

    def count_dots(self) -> int:
        """
        Return the number of dots currently on the paper.
        """
        pass

    def __str__(self):
        """
        Return a string representation of the transparent paper.
        """

        # Find the max x value
        x_max = max([point[1] for point in self.coords])

        # Find the max y value
        y_max = max([point[0] for point in self.coords])

        # Fill the paper with empty values
        paper = np.full((y_max + 1, x_max + 1), ".")

        # Iterate over the coordinates and fill them in
        for point in self.coords:
            paper[point] = "#"

        # Convert array to string
        ret_val = ""

        for j in range(paper.shape[1]):
            for i in range(paper.shape[0]):
                ret_val += paper[i, j]
            ret_val += "\n"

        return ret_val


sample_p = TransPaper("./data/sample.txt")
print(sample_p)

# input_p = TransPaper("./data/input.txt")
