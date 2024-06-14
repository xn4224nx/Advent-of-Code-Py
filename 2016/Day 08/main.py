"""
--- Day 8: Two-Factor Authentication ---

The magnetic strip on the card you swiped encodes a series of instructions for
the screen; these instructions are your puzzle input. The screen is 50 pixels
wide and 6 pixels tall, all of which start off, and is capable of three
somewhat peculiar operations:

    rect AxB turns on all of the pixels in a rectangle at the top-left of the
    screen which is A wide and B tall.

    rotate row y=A by B shifts all of the pixels in row A (0 is the top row)
    right by B pixels. Pixels that would fall off the right end appear at the
    left end of the row.

    rotate column x=A by B shifts all of the pixels in column A (0 is the left
    column) down by B pixels. Pixels that would fall off the bottom appear at
    the top of the column.

Part 1 - How many pixels should be lit?
"""

import numpy as np
import re


class TFAScreen:

    def __init__(self, instruct_fp, s_width, s_height):

        # Define the on and off characters
        self.on_char = '#'
        self.off_char = '.'

        # Receive the screen size
        self.s_width = s_width
        self.s_height = s_height

        # Receive the instructions
        self.instructions = open(instruct_fp).read().splitlines()

        # Initialise the screen as all off
        self.screen = np.full((self.s_height, self.s_width), self.off_char)

    def __str__(self):
        """Output a string representation of the screen."""

        out_str = ""

        for i in range(self.s_height):
            for j in range(self.s_width):
                out_str += self.screen[i, j]
            out_str += "\n"

        return out_str

    def __int__(self):
        """Give a count of the the lights that are on."""
        return len(np.where(self.screen == self.on_char)[0])

    def execute_instruc(self, instruc_str):
        """Take a string instruction and determine what function to run."""

        data_vals = re.search(r"(rect ([0-9]+)x([0-9]+))|(rotate column x="
                              r"([0-9]+) by ([0-9]+))|(rotate row y=([0-9]+) "
                              r"by ([0-9]+))", instruc_str)

        if data_vals.group(1) is not None:
            self.rect(int(data_vals.group(2)), int(data_vals.group(3)))

        elif data_vals.group(7) is not None:
            self.rotate_row(int(data_vals.group(8)), int(data_vals.group(9)))

        elif data_vals.group(4) is not None:
            self.rotate_col(int(data_vals.group(5)), int(data_vals.group(6)))

    def execute_all_instruc(self):
        """Iterate through all instructions given to the class and do them."""

        for instruc_str in self.instructions:
            self.execute_instruc(instruc_str)

    def rect(self, a_wide, b_tall):
        """
        Turns on all of the pixels in a rectangle at the top-left of the
        screen which is A wide and B tall.
        """

        self.screen[:b_tall, :a_wide] = self.on_char

    def rotate_row(self, row_a, shift_b):
        """
        Rotate row y=A by B shifts all of the pixels in row A (0 is the top
        row) right by B pixels. Pixels that would fall off the right end
        appear at the left end of the row.
        """

        self.screen[row_a, :] = \
            np.concatenate((self.screen[row_a, -shift_b:],
                            self.screen[row_a, :-shift_b]))

    def rotate_col(self, col_a, shift_b):
        """
        Rotate column x=A by B shifts all of the pixels in column A (0 is the
        left column) down by B pixels. Pixels that would fall off the bottom
        appear at the top of the column.
        """

        self.screen[:, col_a] = \
            np.concatenate((self.screen[-shift_b:, col_a],
                            self.screen[:-shift_b, col_a]))


input_screen = TFAScreen("data/input.txt", 50, 6)
input_screen.execute_all_instruc()

# Part 1
print(int(input_screen))

# Part 2
print(input_screen)