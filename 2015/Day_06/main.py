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
        self.grid = np.full(grid_shape, start_light_state)
        self.shape = grid_shape

    def count_on_lights(self) -> int:
        """
        Determine how many lights are currently on in the grid.
        """
        return int(np.sum(self.grid))

    def turn_on(self, s_pnt: (int, int), e_pnt: (int, int)):
        """
        Turn on the lights in a rectangle between the start point and
        the end point.
        """
        self.grid[s_pnt[0] : e_pnt[0], s_pnt[1] : e_pnt[1]] = True

    def turn_off(self, s_pnt: (int, int), e_pnt: (int, int)):
        """
        Turn off the lights in a rectangle between the start point and
        the end point.
        """
        self.grid[s_pnt[0] : e_pnt[0], s_pnt[1] : e_pnt[1]] = False

    def toggle(self, s_pnt: (int, int), e_pnt: (int, int)):
        """
        Change the state of the lights in a rectangle between the
        start point and the end point.
        """
        self.grid[s_pnt[0] : e_pnt[0], s_pnt[1] : e_pnt[1]] = np.invert(
            self.grid[s_pnt[0] : e_pnt[0], s_pnt[1] : e_pnt[1]]
        )

    def parse_command(self, raw_command: str) -> dict:
        """
        Take a raw command and extract the command and the coordiantes.
        """
        cords = [int(x) for x in re.findall(r"\d+", raw_command)]

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
            "e_pnt": (cords[2] + 1, cords[3] + 1),
        }

    def exe_single_command(self, raw_command: str):
        """
        Modify the grid based on the raw command given.
        """
        com = self.parse_command(raw_command)

        if com["command"] == cmd.turn_on:
            self.turn_on(com["s_pnt"], com["e_pnt"])

        elif com["command"] == cmd.turn_off:
            self.turn_off(com["s_pnt"], com["e_pnt"])

        else:
            self.toggle(com["s_pnt"], com["e_pnt"])

    def execute_commands(self, cmd_file: str):
        """
        Read all the commands in a file an execute them all.
        """
        for line in open(cmd_file).readlines():
            self.exe_single_command(line)


if __name__ == "__main__":
    decor = LightGrid((1000, 1000), False)
    decor.execute_commands("./data/input.txt")
    print(f"The answer to part 1 = {decor.count_on_lights()}")
