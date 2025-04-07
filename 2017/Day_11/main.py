r"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a
program comes up to you, clearly in distress. "It's my child process," she
says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be
found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you need
to determine the fewest number of steps required to reach him. (A "step" means
to move from the hex you are in to any adjacent hex.)

For example:

    -   ne,ne,ne is 3 steps away.
    -   ne,ne,sw,sw is 0 steps away (back where you started).
    -   ne,ne,s,s is 2 steps away (se,se).
    -   se,sw,se,sw,sw is 3 steps away (s,s,sw).

PART 1: Starting where he started, you need to determine the fewest number of
        steps required to reach him.

PART 2: How many steps away is the furthest he ever got from his starting
        position?
"""

from pathlib import Path


class HexGrid:
    def __init__(self, direction_file: str):
        self.path = Path(direction_file).read_text().strip().split(",")

    def min_len_path(self) -> (int, int):
        """
        Find the minimum length required to reach the final destination of the
        path through the hex grid. Also find the maximum distance from the
        center the path takes.

        return the minimum and maximum.

        Algorithm taken from: https://www.redblobgames.com/grids/hexagons/
        """
        max_dist = 0
        n_dir = 0
        se_dir = 0

        # Iterate over the path and calculate the count in the two hex directions
        for curr_p in self.path:

            if curr_p == "n":
                n_dir += 1

            elif curr_p == "s":
                n_dir -= 1

            elif curr_p == "ne":
                n_dir += 1
                se_dir += 1

            elif curr_p == "se":
                se_dir += 1

            elif curr_p == "nw":
                se_dir -= 1

            elif curr_p == "sw":
                n_dir -= 1
                se_dir -= 1

            else:
                raise Exception(f'Unknown direction "{curr_p}"')

            curr_dist = int((abs(n_dir) + abs(se_dir) + abs(n_dir - se_dir)) / 2)

            # Check for a maximum distance
            if curr_dist > max_dist:
                max_dist = curr_dist

        return curr_dist, max_dist


if __name__ == "__main__":
    min_dist, max_dist = HexGrid("./data/input.txt").min_len_path()
    print(f"Part 1 = {min_dist}\nPart 2 = {max_dist}")
