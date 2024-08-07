"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house
decorating contest year after year, you've decided to deploy one
million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year,
Santa has mailed you instructions on how to display the ideal
lighting configuration.

Lights in your grid are numbered from 0 to 999 in each
direction; the lights at each corner are at 0,0, 0,999, 999,999,
and 999,0. The instructions include whether to turn on, turn off,
or toggle various inclusive ranges given as coordinate pairs.
Each coordinate pair represents opposite corners of a rectangle,
inclusive; a coordinate pair like 0,0 through 2,2 therefore
refers to 9 lights in a 3x3 square. The lights all start turned
off.

To defeat your neighbors this year, all you have to do is set up
your lights by doing the instructions Santa sent you in order.

PART 1: After following the instructions, how many lights are
		lit?
"""

import numpy as np
import re
from enum import Enum

cmd = Enum("cmd", ["turn_on", "turn_off", "toggle"])


class LightGrid:
    """
    A matrix of boolean values that represent a grid of lights. True means
    that light is on and false off.
    """

    def __init__(self, grid_shape: (int, int), start_light_state: bool):
        self.grid = numpy.full(grid_shape, start_light_state)
        self.shape = grid_shape

    def count_on_lights(self) -> int:
        """
        Determine how many lights are currently on in the grid.
        """
        return np.sum(self.grid)

    def turn_off(self, s_pnt: (int, int), e_pnt: (int, int)):
        """
        Turn off the lights in a rectangle between the start point and
        the end point.
        """
        self.grid[s_pnt[0] : e_pnt[0], s_pnt[1] : e_pnt[1]] = False

    def turn_on(self, s_pnt: (int, int), e_pnt: (int, int)):
        """
        Turn on the lights in a rectangle between the start point and
        the end point.
        """
        self.grid[s_pnt[0] : e_pnt[0], s_pnt[1] : e_pnt[1]] = True

    def toggle(self, s_pnt: (int, int), e_pnt: (int, int)):
        """
        Change the state of the lights in a rectangle between the
        start point and the end point.
        """
        self.grid[s_pnt[0] : e_pnt[0], s_pnt[1] : e_pnt[1]] = np.invert(
            self.grid[s_pnt[0] : e_pnt[0], s_pnt[1] : e_pnt[1]]
        )

    def parse_command(raw_command: str) -> dict:
        """
        Take a raw command and extract the command and the coordiantes.
        """
        cords = re.findall(r"\d+", raw_command)

        if "turn on" in raw_command:
            command = cmd.turn_on

        elif "toggle" in raw_command:
            command = cmd.toggle

        elif "turn off" in raw_command:
            command = cmd.turn_off

        else:
            raise Exception("Key command not found")

        return {
            "command": command,
            "s_pnt": (cords[0], cords[1]),
            "e_pnt": (cords[2], cords[3]),
        }

    def execute_command(raw_command: str):
        """
        Modify the grid based on the raw command given.
        """
        pass


if __name__ == "__main__":
    pass
