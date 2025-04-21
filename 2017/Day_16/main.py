"""
--- Day 16: Permutation Promenade ---

You come upon a very unusual sight; a group of programs here appear to be
dancing.

There are sixteen programs in total, named a through p. They start by standing
in a line: a stands in position 0, b stands in position 1, and so on until p,
which stands in position 15.

The programs' dance consists of a sequence of dance moves:

    -   Spin, written sX, makes X programs move from the end to the front, but
        maintain their order otherwise. (For example, s3 on abcde produces
        cdeab).

    -   Exchange, written xA/B, makes the programs at positions A and B swap
        places.

    -   Partner, written pA/B, makes the programs named A and B swap places.

For example, with only five programs standing in a line (abcde), they could do
the following dance:

    -   s1, a spin of size 1: eabcd.

    -   x3/4, swapping the last two programs: eabdc.

    -   pe/b, swapping programs e and b: baedc.

After finishing their dance, the programs end up in order baedc.

PART 1: You watch the dance for a while and record their dance moves (your
        puzzle input). In what order are the programs standing after their
        dance?
"""

from collections import deque


class ProgramDance:
    def __init__(self, initial_progs: str, instruc_file: str):
        pass

    def spin(self, magnitude: int):
        """
        Make a number of programs move from the end to the front
        """
        pass

    def exchange(self, idx_a: int, idx_b: int):
        """
        Swap programs by index.
        """
        pass

    def partner(self, prog_a: str, prog_b: str):
        """
        Swap programs by value.
        """
        pass

    def execute_command(self, com: dict[str:str]):
        """
        Execute one of the commands, spin, exchange or partner.
        """
        pass

    def run_all_commands(self) -> str:
        """
        Using the instructions file find the final order of the programs.
        """
        pass


if __name__ == "__main__":
    pass
