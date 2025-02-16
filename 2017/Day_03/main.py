"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location
marked 1 and then counting up while spiraling outward. For example, the first
few squares are allocated like this:

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data must
be carried back to square 1 (the location of the only access port for this
memory system) by programs that can only move up, down, left, or right. They
always take the shortest path: the Manhattan Distance between the location of
the data and square 1.

For example:

    -   Data from square 1 is carried 0 steps, since it's at the access port.
    -   Data from square 12 is carried 3 steps, such as: down, left, left.
    -   Data from square 23 is carried only 2 steps: up twice.
    -   Data from square 1024 must be carried 31 steps.

PART 1: How many steps are required to carry the data from the square identified
        in your puzzle input all the way to the access port?
"""


class SpiralMemory:
    def __init__(self, max_val: int):
        self.max_val = max_val

    def moves_to_exit(self) -> int:
        """
        Calculate the manhattan distance that a square at `max_val` would need
        to travel to get to the exit square at one.
        """
        if self.max_val in [0, 1]:
            return self.max_val

        # What ring in the spiral is the number located?
        ring = -(-(self.max_val**0.5) // 1) // 2

        # What is the remaining steps to take from the start point in the ring?
        rem_steps = self.max_val - ((2 * ring - 1) ** 2) % (4 * (2 * ring - 1) + 4)

        # What is the offset from the centre of each ring side
        offset = abs(((rem_steps % (2 * ring))) - ring)

        # What is the manhattan distance to the centre?
        return int(offset + ring)


if __name__ == "__main__":
    print(f"Part 1 = {SpiralMemory(325489).moves_to_exit()}")
