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

    def fold_paper(self, axis: str, fold_pos: int):
        """
        Fold the paper along a certain line defined by `axis` and `fold_pos`,
        recalculate the dots new position and remove duplicates.
        """

        new_coords = []

        # For each coordinate
        for (y_pnt, x_pnt) in self.coords:

            # If it is outside the x fold line change the y coord
            if axis == "x" and y_pnt > fold_pos:
                new_coords.append((2*fold_pos - y_pnt, x_pnt))

            # If it is outside the y fold line change the x coord
            elif axis == "y" and x_pnt > fold_pos:
                new_coords.append((y_pnt, 2*fold_pos - x_pnt))

            else:
                new_coords.append((y_pnt, x_pnt))

        # Deduplicate the points
        new_coords = list(set(new_coords))

        self.coords = new_coords

    def execute_fold_instructs(self, num: int = None):
        """
        Execute a number of the fold instructions given in the data file.
        `num` is the number of fold instructions to execute. None indicates they
        all will be done.
        """

        # Check for limited number of fold executions
        if num is None:
            num = len(self.folds)

        # Execute the specified folds
        for idx in range(num):

            f_axis = self.folds[idx][0]
            f_mag = self.folds[idx][1]

            self.fold_paper(f_axis, f_mag)

    def count_dots(self) -> int:
        """
        Return the number of dots currently on the paper.
        """
        return len(self.coords)

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


# Part 1
input_p = TransPaper("./data/input.txt")
input_p.execute_fold_instructs(1)
print(f"The answer to part one is: {input_p.count_dots()}")

# Part 2
input_p = TransPaper("./data/input.txt")
input_p.execute_fold_instructs()
print(input_p)