# -*- coding: utf-8 -*-
"""

--- Day 9: Rope Bridge ---

Simulate your complete hypothetical series of motions.
How many positions does the tail of the rope visit at least once?

Created on Fri Dec  9 16:41:46 2022

@author: FAKENAME
"""

import numpy as np


class Rope:
    """
    Simulation of a rope of planc length

    """

    def __init__(self):

        # Current Coordinates of the head of the rope
        self.h_pos = [0, 0]

        # Current Coordinates of the tail of the rope
        self.t_pos = [0, 0]

        # Current Instructions
        self.direction = None
        self.magnitude = None

        # History of where the rope has been
        self.h_hist = [(0, 0)]
        self.t_hist = [(0, 0)]

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
        self.h_pos[self.direction] += np.sign(self.magnitude)

        # Check if the tail is too far away from the head
        if not self.is_tail_close():

            # And if it is move it closer to the head
            self.move_tail_closer()

        # Save the positions of the head & tail of the rope after the move
        self.h_hist.append(tuple(self.h_pos))
        self.t_hist.append(tuple(self.t_pos))

    def is_tail_close(self):
        """
        Check that the tails is within one square of the head of the rope
        """

        if (self.h_pos[0]-2 < self.t_pos[0] < self.h_pos[0]+2) \
                and (self.h_pos[1]-2 < self.t_pos[1] < self.h_pos[1]+2):
            return True
        else:
            return False

    def move_tail_closer(self):
        """
        Move the tail closer to the head
        """

        # Upper row Tails
        if self.t_pos[1] > self.h_pos[1] + 1:
            self.t_pos[1] -= 1
            self.t_pos[0] = self.h_pos[0]

        # Lower Row Tails
        elif self.t_pos[1] < self.h_pos[1] - 1:
            self.t_pos[1] += 1
            self.t_pos[0] = self.h_pos[0]

        # Right Outer Column Tails
        elif self.t_pos[0] > self.h_pos[0] + 1:
            self.t_pos[0] -= 1
            self.t_pos[1] = self.h_pos[1]

        # Left Outer Column Tails
        elif self.t_pos[0] < self.h_pos[0] - 1:
            self.t_pos[0] += 1
            self.t_pos[1] = self.h_pos[1]


# Load Instructions
instruct_ls = open("input.txt", "r").read().splitlines()

# Parse Instructions
instruct_ls = [tuple(inst.split()) for inst in instruct_ls]
instruct_ls = [(x, int(y)) for x,y in instruct_ls ]

# Run a test
test_rope = Rope()

# Run the rope pull according to the instructions
for instr in instruct_ls:
    test_rope.pull_rope(instr)

# Count the unique positions of the tail end
print(f"Unique positions of the tail end = {len(set(test_rope.t_hist))}")
