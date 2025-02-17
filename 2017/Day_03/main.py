"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location
marked 1 and then counting up while spiraling outward. For example, the first
few squares are allocated like this:

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data must
be carried back to square 1 (the location of the only access port for this
memory system) by programs that can only move up, down, left, or right. They
always take the shortest path: the Manhattan Distance between the location of
the data and square 1.

For example:

    -   Data from square 1 is carried 0 steps, since it's at the access port.
    -   Data from square 12 is carried 3 steps, such as: down, left, left.
    -   Data from square 23 is carried only 2 steps: up twice.
    -   Data from square 1024 must be carried 31 steps.

PART 1: How many steps are required to carry the data from the square identified
        in your puzzle input all the way to the access port?

As a stress test on the system, the programs here clear the grid and then store
the value 1 in square 1. Then, in the same allocation order as shown above, they
store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

    -   Square 1 starts with the value 1.

    -   Square 2 has only one adjacent filled square (with value 1), so it also
        stores 1.

    -   Square 3 has both of the above squares as neighbors and stores the sum
        of their values, 2.

    -   Square 4 has all three of the aforementioned squares as neighbors and
        stores the sum of their values, 4.

    -   Square 5 only has the first and fourth squares as neighbors, so it gets
        the value 5.

Once a square is written, its value does not change. Therefore, the first few
squares would receive the following values:

    147  142  133  122   59
    304    5    4    2   57
    330   10    1    1   54
    351   11   23   25   26
    362  747  806--->   ...

PART 2: What is the first value written that is larger than your puzzle input?
"""

import numpy as np
import math


class SpiralMemory:
    def __init__(self, max_val: int = 0):
        self.max_val = max_val

    def coord_of_step(self, step_idx: int) -> (int, int):
        """
        Find the coordinates of a step in the sprial assuming the origin is
        point (0,0).
        """
        # Calculate the ring characteristics
        ring = int(-(-(step_idx**0.5) // 1) // 2)
        ring_side_len = int(2 * ring + 1)
        ring_final_val = int((ring_side_len) ** 2)

        # Calculate the value at each of the corners of the ring
        bot_left = ring_final_val - (ring_side_len - 1)
        top_left = ring_final_val - 2 * (ring_side_len - 1)
        top_rght = ring_final_val - 3 * (ring_side_len - 1)

        # Using the above infomation calculate the coordinates of the point

        # Test to see if this step is on a corner
        if step_idx == ring_final_val:
            pnt = (ring, -ring)

        elif step_idx == bot_left:
            pnt = (-ring, -ring)

        elif step_idx == top_left:
            pnt = (-ring, ring)

        elif step_idx == top_rght:
            pnt = (ring, ring)

        # Bottow row points
        elif ring_final_val > step_idx > bot_left:
            pnt = (step_idx - bot_left - ring_side_len // 2, -ring)

        # Top row points
        elif top_left > step_idx > top_rght:
            pnt = ((top_rght + ring_side_len // 2) - step_idx, ring)

        # Left column points
        elif bot_left > step_idx > top_left:
            pnt = (-ring, (top_left + ring_side_len // 2) - step_idx)

        # Right column points
        elif top_rght > step_idx:
            pnt = (ring, step_idx - top_rght + ring_side_len // 2)

        else:
            raise Exception(f"Step {step_idx} could not be placed at a point.")

        return (int(pnt[0]), int(pnt[1]))

    def moves_to_exit(self, step_idx: int) -> int:
        """
        Calculate the manhattan distance that a square at `max_val` would need
        to travel to get to the exit square at one.
        """

        # What are the coordinates of this step?
        coord = self.coord_of_step(step_idx)

        # Return the sum of the magnitudes of the x and y values.
        return int(abs(coord[0]) + abs(coord[1]))

    def find_first_gt_max_val(self) -> int:
        """
        Assuming the squares start at one and have their value decided by the
        sum of already created adjacent squares. What is the first value
        created larger than the max value? This corresponds to the OEIS sequence
        A141481. https://oeis.org/A141481
        """
        step_idx = 2
        pnt_vals = {(0, 0): 1}

        # Generate the values for each step
        while True:
            pnt = self.coord_of_step(step_idx)

            # Define the possible adjacent points to the current one
            possible_adj_pnts = [
                (pnt[0] + 1, pnt[1] + 1),
                (pnt[0], pnt[1] + 1),
                (pnt[0] - 1, pnt[1] + 1),
                (pnt[0] + 1, pnt[1]),
                (pnt[0] - 1, pnt[1]),
                (pnt[0] + 1, pnt[1] - 1),
                (pnt[0], pnt[1] - 1),
                (pnt[0] - 1, pnt[1] - 1),
            ]

            # Calculate the value for this point
            pnt_sum = 0
            for adj_pnt in possible_adj_pnts:
                if adj_pnt in pnt_vals:
                    pnt_sum += pnt_vals[adj_pnt]

            # Check for a solution
            if pnt_sum > self.max_val:
                return pnt_sum

            else:
                pnt_vals[pnt] = pnt_sum
                step_idx += 1


if __name__ == "__main__":
    strg = SpiralMemory(325489)
    print(f"Part 1 = {strg.moves_to_exit(strg.max_val)}")
    print(f"Part 2 = {strg.find_first_gt_max_val()}")
