"""
--- Day 19: A Series of Tubes ---

Somehow, a network packet got lost and ended up here. It's trying to follow a
routing diagram (your puzzle input), but it's confused about where to go.

Its starting point is just off the top of the diagram. Lines (drawn with |, -,
and +) show the path it needs to take, starting by going down onto the only
line connected to the top of the diagram. It needs to follow this path until it
reaches the end (located somewhere within the diagram) and stop there.

Sometimes, the lines cross over each other; in these cases, it needs to
continue going the same direction, and only turn left or right when there's no
other option. In addition, someone has left letters on the line; these also
don't change its direction, but it can use them to keep track of where it's
been. For example:

     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+

Given this diagram, the packet needs to take the following path:

        -   Starting at the only line touching the top of the diagram, it must
            go down, pass through A, and continue onward to the first +.

        -   Travel right, up, and right, passing through B in the process.

        -   Continue down (collecting C), right, and up (collecting D).

        -   Finally, go all the way left through E and stopping at F.

Following the path to the end, the letters it sees on its path are ABCDEF.

PART 1: The little packet looks up at you, hoping you can help it find the way.
        What letters will it see (in the order it would see them) if it follows
        the path? (The routing diagram is very wide; make sure you view it
        without line wrapping.)

The packet is curious how many steps it needs to go.

For example, using the same routing diagram from the example above...

     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+

...the packet would go:

        -   6 steps down (including the first line at the top of the diagram).
        -   3 steps right.
        -   4 steps up.
        -   3 steps right.
        -   4 steps down.
        -   3 steps right.
        -   2 steps up.
        -   13 steps left (including the F it stops on).

This would result in a total of 38 steps.

PART 2: How many steps does the packet need to go?
"""

import string


class Network:
    def __init__(self, datafile: str):
        self.plan = {}
        self.loc = None
        self.direct = 1j

        with open(datafile, "r") as fp:
            for line_idx, line in enumerate(fp.readlines()):
                for char_idx, char in enumerate(line):
                    if not char.isspace():
                        self.plan[(char_idx, line_idx)] = char

                        # Set the top left most char as the start point
                        if self.loc is None:
                            self.loc = (char_idx, line_idx)

    def step(self):
        """
        Move one step along the path through the network.
        """
        nxt_loc = (self.loc[0] + self.direct.real, self.loc[1] + self.direct.imag)
        assert nxt_loc in self.plan

        # Continue along in the same direction
        if self.plan[nxt_loc] in ["-", "|"]:
            self.loc = nxt_loc

        # Work out where to go at a junction or letter
        elif self.plan[nxt_loc] in "+" + string.ascii_uppercase:

            # Find the occupied location other than the current
            possible_locs = [
                (nxt_loc[0], nxt_loc[1] - 1),
                (nxt_loc[0] - 1, nxt_loc[1]),
                (nxt_loc[0] + 1, nxt_loc[1]),
                (nxt_loc[0], nxt_loc[1] + 1),
            ]

            # Remove the previous location from the possible next moves
            possible_locs.remove(self.loc)

            # Find which possible location that has a non-space value
            for loc in possible_locs:
                if loc in self.plan and loc != self.loc:
                    self.loc = nxt_loc
                    nxt_loc = loc
                    self.direct = complex(
                        nxt_loc[0] - self.loc[0], nxt_loc[1] - self.loc[1]
                    )
                    break

            # Indicate there is nowhere left to go after the next step
            else:
                self.direct = 0
                self.loc = nxt_loc

    def path_letters(self) -> str:
        """
        Follow the path through the network and collect the letters that are
        encountered. Also return the number of steps in the path.
        """
        seen = ""
        steps = 0

        while self.direct != 0:
            if self.plan[self.loc] in string.ascii_uppercase:
                seen += self.plan[self.loc]
            self.step()
            steps += 1

        return (seen + self.plan[self.loc], steps + 1)


if __name__ == "__main__":
    path, path_len = Network("./data/input.txt").path_letters()
    print(f"Part 1 = {path}\nPart 2 = {path_len}\n")
