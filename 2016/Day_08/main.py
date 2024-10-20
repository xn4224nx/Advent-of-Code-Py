"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an
implementation of two-factor authentication after a long game of requirements
telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a
nearby desk). Then, it displays a code on a little screen, and you type that
code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken
everything apart and figured out how it works. Now you just have to work out
what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for
the screen; these instructions are your puzzle input. The screen is 50 pixels
wide and 6 pixels tall, all of which start off, and is capable of three
somewhat peculiar operations:

    -   rect AxB turns on all of the pixels in a rectangle at the top-left of
        the screen which is A wide and B tall.

    -   rotate row y=A by B shifts all of the pixels in row A (0 is the top
        row) right by B pixels. Pixels that would fall off the right end appear
        at the left end of the row.

    -   rotate column x=A by B shifts all of the pixels in column A (0 is the
        left column) down by B pixels. Pixels that would fall off the bottom
        appear at the top of the column.

As you can see, this display technology is extremely powerful, and will soon
dominate the tiny-code-displaying-screen market. That's what the advertisement
on the back of the display tries to convince you, anyway.

PART 1: There seems to be an intermediate check of the voltage used by the
        display: after you swipe your card, if the screen did work, how many
        pixels should be lit?
"""

import numpy as np
from collections import deque
import re


class SecurityScreen:

    def __init__(self, screen_size: (int, int)):
        # Define the screen and set every pixel as off
        self.scrn = np.full(screen_size, False, dtype=bool)
        self.instructs = []

    def read_instru(self, file_path):
        """
        Open a file with screen change instructions and save a copy of the
        raw lines into the class instance.
        """
        with open(file_path) as fp:
            for line in fp.readlines():
                self.instructs.append(line.strip())

    def turn_on_rect(self, A: int, B: int):
        """
        Set a rectangle of the screen to be on, this rectangle starts from
        the origin 0,0.
        """
        self.scrn[:A, :B] = True

    def rotate_row(self, A: int, B: int):
        """
        Spin a row of the screen a set number of positions.
        """
        row = deque(self.scrn[:, A])

        # Rotate the row
        row.rotate(B)

        # Set the new row
        self.scrn[:, A] = row

    def rotate_col(self, A: int, B: int):
        """
        Spin a column of the screen as set number of positions.
        """
        col = deque(self.scrn[A, :])

        # Rotate the col
        col.rotate(B)

        # Set the new col
        self.scrn[A, :] = col

    def show_screen(self) -> str:
        """
        Return the screens current state as a string of . and #, where the
        former is off and the latter is on. The coordinate 0,0 is in the top
        left hand corner of the image.
        """
        screen = ""

        for x in range(self.scrn.shape[1]):
            for y in range(self.scrn.shape[0]):
                if self.scrn[y][x]:
                    screen += "#"
                else:
                    screen += "."
            screen += "\n"

        return screen

    def execute_instr(self, instr: str):
        """
        Take a string instruction and execute a method based on it.
        """
        nums = [int(x) for x in re.findall(r"[0-9]+", instr)]

        if "rect" in instr:
            self.turn_on_rect(nums[0], nums[1])

        elif "rotate column" in instr:
            self.rotate_col(nums[0], nums[1])

        elif "rotate row" in instr:
            self.rotate_row(nums[0], nums[1])
        else:
            raise Exception(f"Command '{instr}' not recognised!")

    def execute_all_instr(self):
        """
        Execute all the string based instructions.
        """
        for instr in self.instructs:
            self.execute_instr(instr)

    def count_on_pixels(self) -> int:
        """
        Return the numerical count of the on pixels.
        """
        return np.sum(self.scrn)


if __name__ == "__main__":
    pass
