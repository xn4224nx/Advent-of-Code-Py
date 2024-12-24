"""
--- Day 18: Like a Rogue ---

As you enter this room, you hear a loud click! Some of the tiles in the floor
here seem to be pressure plates for traps, and the trap you just triggered has
run out of... whatever it tried to do to you. You doubt you'll be so lucky next
time.

Upon closer examination, the traps and safe tiles in this room seem to follow a
pattern. The tiles are arranged into rows that are all the same width; you take
note of the safe tiles (.) and traps (^) in the first row (your puzzle input).

The type of tile (trapped or safe) in each row is based on the types of the
tiles in the same position, and to either side of that position, in the previous
row. (If either side is off either end of the row, it counts as "safe" because
there isn't a trap embedded in the wall.)

For example, suppose you know the first row (with tiles marked by letters) and
want to determine the next row (with tiles marked by numbers):

    ABCDE
    12345

The type of tile 2 is based on the types of tiles A, B, and C; the type of tile
5 is based on tiles D, E, and an imaginary "safe" tile. Let's call these three
tiles from the previous row the left, center, and right tiles, respectively.
Then, a new tile is a trap only in one of the following situations:

    -   Its left and center tiles are traps, but its right tile is not.

    -   Its center and right tiles are traps, but its left tile is not.

    -   Only its left tile is a trap.

    -   Only its right tile is a trap.

In any other situation, the new tile is safe.

PART 1: Starting with the map in your puzzle input, in a total of 40 rows
        (including the starting row), how many safe tiles are there?
"""


class TrapRoom:
    def __init__(self, data_file: str):
        """
        Read the first row of floor tiles from the data file.
        """
        pass

    def show(self) -> str:
        """
        Provide a string representation of the trap room in its current state.
        """
        pass

    def gen_next_row(self, rows: int):
        """
        Create the next row of tiles in the room
        """
        pass

    def count_safe_tiles(self) -> int:
        """
        Return the total number of safe tiles in the trap room.
        """
        pass


if __name__ == "__main__":
    pass
