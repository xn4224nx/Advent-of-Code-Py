# -*- coding: utf-8 -*-
"""

--- Day 9: Rope Bridge ---

Part 2 - The rope has many segments

Simulate your complete hypothetical series of motions.
How many positions does the tail of the rope visit at least once?

Created on Fri Dec  9 16:41:46 2022

@author: FAKENAME
"""

import numpy as np


class Rope:
    """
    Simulation of a rope of planc length rope_parts

    """

    def __init__(self, rope_parts):

        # How many sections does the rope have
        self.rope_parts = rope_parts

        # Current Coordinates of the of the rope sections
        self.r_pos = [[0, 0] for i in range(self.rope_parts)]

        # Current Instructions
        self.direction = None
        self.magnitude = None

        # History of where the rope has been
        self.r_hist = [[(0, 0)] for i in range(self.rope_parts)]

    def pull_rope(self, instruc):
        """
        Recive the rope pull instructions as a tuple of a char and an int.
        """

        self.magnitude = instruc[1]

        # Change magniture based on direction
        if instruc[0] in ['D', 'L']:
            self.magnitude *= -1

        # set which value in the h_pos is going to change
        if instruc[0] in ['U', 'D']:
            self.direction = 1  # y coord

        elif instruc[0] in ['L', 'R']:
            self.direction = 0  # x coord

        # Run multiple steps in the rope movement
        for i in range(abs(self.magnitude)):
            self.rope_pull_step()

    def rope_pull_step(self):
        """
        Pull the rope one magnitude in the current direction
        """

        # Move the head of the rope by either 1 or -1
        self.r_pos[0][self.direction] += np.sign(self.magnitude)

        # For each proceeding segment test if it is close enough to
        # the proceeding part
        for i in range(self.rope_parts-1):

            # Check if this segment is too far away from the previous
            if not self.is_tail_seg_close(i, i+1):

                # If so move it
                self.move_tail_seg_closer(i, i+1)

        # Save the positions of the head & tail of the rope after the move
        for i in range(self.rope_parts):
            self.r_hist[i].append(tuple(self.r_pos[i]))

    def is_tail_seg_close(self, c_idx, n_idx):
        """
        Check that the next segment of the rope is within one square
        of the current section of the rope.
        """

        if (self.r_pos[c_idx][0]-2 < self.r_pos[n_idx][0]
            < self.r_pos[c_idx][0]+2) \
                and (self.r_pos[c_idx][1]-2 < self.r_pos[n_idx][1]
                     < self.r_pos[c_idx][1]+2):
            return True
        else:
            return False

    def move_tail_seg_closer(self, c_idx, n_idx):
        """
        Move the tail closer to the head
        """

        # Upper row Tails
        if self.r_pos[n_idx][1] > self.r_pos[c_idx][1] + 1:
            self.r_pos[n_idx][1] = self.r_pos[c_idx][1] + 1
            self.r_pos[n_idx][0] = self.r_pos[c_idx][0]

        # Lower Row Tails
        elif self.r_pos[n_idx][1] < self.r_pos[c_idx][1] - 1:
            self.r_pos[n_idx][1] = self.r_pos[c_idx][1] - 1
            self.r_pos[n_idx][0] = self.r_pos[c_idx][0]

        # Right Outer Column Tails
        if self.r_pos[n_idx][0] > self.r_pos[c_idx][0] + 1:
            self.r_pos[n_idx][0] = self.r_pos[c_idx][0] + 1
            self.r_pos[n_idx][1] = self.r_pos[c_idx][1]

        # Left Outer Column Tails
        elif self.r_pos[n_idx][0] < self.r_pos[c_idx][0] - 1:
            self.r_pos[n_idx][0] = self.r_pos[c_idx][0] - 1
            self.r_pos[n_idx][1] = self.r_pos[c_idx][1]


# Load Instructions
instruct_ls = open("test2.txt", "r").read().splitlines()

# Parse Instructions
instruct_ls = [tuple(inst.split()) for inst in instruct_ls]
instruct_ls = [(x, int(y)) for x, y in instruct_ls]

# Run a test
test_rope = Rope(10)

# Run the rope pull according to the instructions
for i in range(len(instruct_ls)):
    test_rope.pull_rope(instruct_ls[i])

    # if i > 0:
    #     break

# Count the unique positions of the tail end
print(f"Unique positions of the tail end = {len(set(test_rope.r_hist[9]))}")
