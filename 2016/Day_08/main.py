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


class SecurityScreen:

    def __init__(self, screen_size: (int, int)):
        pass

    def read_instru(self, file_path):
        pass

    def turn_on_rect(self, A: int, B: int):
        pass

    def rotate_row(self, A: int, B: int):
        pass

    def rotate_col(self, A: int, B: int):
        pass

    def show_screen(self) -> str:
        pass

    def execute_instr(self, str):
        pass

    def execute_all_instr(self):
        pass

    def count_on_pixels(self) -> int:
        pass


if __name__ == "__main__":
    pass
