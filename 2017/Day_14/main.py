"""
--- Day 14: Disk Defragmentation ---

Suddenly, a scheduled job activates the system's disk defragmenter. Were the
situation different, you might sit and watch it for a while, but today, you
just don't have that kind of time. It's soaking up valuable system resources
that are needed elsewhere, and so the only option is to help it finish its task
as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid is
either free or used. On this disk, the state of the grid is tracked by the bits
in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single row
in the grid; each hash contains 128 bits which correspond to individual grid
squares. Each bit of a hash indicates whether that square is free (0) or used
(1).

The hash inputs are a key string (your puzzle input), a dash, and a number from
0 to 127 corresponding to the row. For example, if your key string were
flqrgnkx, then the first row would be given by the bits of the knot hash of
flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and so
on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal
digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128
bits. To convert to bits, turn each hexadecimal digit to its equivalent binary
value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f
becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal
would begin with 10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx appear
as follows, using # to denote used squares, and . to denote free ones:

    ##.#.#..-->
    .#.#.#.#
    ....#.#.
    #.#.##.#
    .##.#...
    ##..#..#
    .#...#..
    ##.#.##.-->
    |      |
    V      V

In this example, 8108 squares are used across the entire 128x128 grid.

PART 1: Given your actual key string, how many squares are used?

Now, all the defragmenter needs to know is the number of regions. A region is a
group of used squares that are all adjacent, not including diagonals. Every
used square is in exactly one region: lone used squares form their own isolated
regions, while several adjacent squares all count as a single region.

In the example above, the following nine regions are visible, each marked with
a distinct digit:

    11.2.3..-->
    .1.2.3.4
    ....5.6.
    7.8.55.9
    .88.5...
    88..5..8
    .8...8..
    88.8.88.-->
    |      |
    V      V

Of particular interest is the region marked 8; while it does not appear
contiguous in this small view, all of the squares marked 8 are connected when
considering the whole 128x128 grid. In total, in this example, 1242 regions are
present.

PART 2: How many regions are present given your key string?
"""

from knothash import KnotHash


class DiskDefrag:
    def __init__(self, seed: str):
        self.size = 128
        self.rows = [KnotHash(f"{seed}-{x}").calc_digest() for x in range(self.size)]
        self.rows = [f"{int(x, base=16):0128b}" for x in self.rows]
        self.rows = [[int(x) for x in y] for y in self.rows]

    def num_used_sqrs(self) -> int:
        """
        Count the number of on squares.
        """
        return sum([sum(x) for x in self.rows])

    def find_adj_pnts(self, pnt: (int, int)) -> list[(int, int)]:
        """
        Get the adjacent points to this point that have the value 1.
        """
        adj_pnts = []

        # Above
        if pnt[0] > 0 and self.rows[pnt[0] - 1][pnt[1]] == 1:
            adj_pnts.append((pnt[0] - 1, pnt[1]))

        # Below
        if pnt[0] < self.size - 1 and self.rows[pnt[0] + 1][pnt[1]] == 1:
            adj_pnts.append((pnt[0] + 1, pnt[1]))

        # Left
        if pnt[1] > 0 and self.rows[pnt[0]][pnt[1] - 1] == 1:
            adj_pnts.append((pnt[0], pnt[1] - 1))

        # Right
        if pnt[1] < self.size - 1 and self.rows[pnt[0]][pnt[1] + 1] == 1:
            adj_pnts.append((pnt[0], pnt[1] + 1))

        return adj_pnts

    def group_count(self) -> int:
        """
        Count the number of groups in the defrag
        """
        grouped_pnts = set()
        grp_count = 0

        # Check each point in the Disk
        for row_idx in range(self.size):
            for col_idx in range(self.size):
                pnt = (row_idx, col_idx)

                # Only 1's can be part of a group
                if self.rows[row_idx][col_idx] == 0:
                    continue

                # Ignore points that have already been assigned a group
                if pnt in grouped_pnts:
                    continue

                # Recursively search adjacent points for 1's
                points_to_search = {pnt}
                while points_to_search:
                    next_points = set()

                    # For each next point generate the adjacent points
                    for n_pnt in points_to_search:
                        grouped_pnts.add(n_pnt)

                        for a_pnt in self.find_adj_pnts(n_pnt):
                            if a_pnt not in grouped_pnts:
                                next_points.add(a_pnt)

                    points_to_search = next_points

                # Increase the group count
                grp_count += 1

        return grp_count


if __name__ == "__main__":
    print(
        f"Part 1 = {DiskDefrag('ffayrhll').num_used_sqrs()}\n"
        f"Part 2 = {DiskDefrag('ffayrhll').group_count()}\n"
    )
