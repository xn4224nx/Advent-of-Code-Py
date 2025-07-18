"""
--- Day 3: No Matter How You Slice It ---

The Elves managed to locate the chimney-squeeze prototype fabric for Santa's
suit (thanks to someone who helpfully wrote its box IDs on the wall of the
warehouse in the middle of the night). Unfortunately, anomalies are still
affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least
1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's
suit. All claims have an ID and consist of a single rectangle with edges
parallel to the edges of the fabric. Each claim's rectangle is defined as
follows:

        -   The number of inches between the left edge of the fabric and the
            left edge of the rectangle.

        -   The number of inches between the top edge of the fabric and the top
            edge of the rectangle.

        -   The width of the rectangle in inches.

        -   The height of the rectangle in inches.

A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3
inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4
inches tall. Visually, it claims the square inches of fabric represented by #
(and ignores the square inches of fabric represented by .) in the diagram
below:

        ...........
        ...........
        ...#####...
        ...#####...
        ...#####...
        ...#####...
        ...........
        ...........
        ...........

The problem is that many of the claims overlap, causing two or more claims to
cover part of the same areas. For example, consider the following claims:

        #1 @ 1,3: 4x4
        #2 @ 3,1: 4x4
        #3 @ 5,5: 2x2

Visually, these claim the following areas:

        ........
        ...2222.
        ...2222.
        .11XX22.
        .11XX22.
        .111133.
        .111133.
        ........

The four square inches marked with X are claimed by both 1 and 2. (Claim 3,
while adjacent to the others, does not overlap either of them.)

PART 1: If the Elves all proceed with their own plans, none of them will have
        enough fabric. How many square inches of fabric are within two or more
        claims?

Amidst the chaos, you notice that exactly one claim doesn't overlap by even a
single square inch of fabric with any other claim. If you can somehow draw
attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are
made.

PART 2: What is the ID of the only claim that doesn't overlap?
"""

import re


class FabricSlicer:
    def __init__(self, rect_def_file: str):
        self.coverage = {}

        with open(rect_def_file, "r") as fp:
            for line in fp.readlines():

                # Extract all numbers from the line
                nums = [int(x) for x in re.findall(r"\d+", line)]

                # Determine the points that this piece of fabric covers
                for x_idx in range(nums[1], nums[1] + nums[3]):
                    for y_idx in range(nums[2], nums[2] + nums[4]):
                        point = (x_idx, y_idx)

                        # Note that this piece of fabric is on this point
                        if point in self.coverage:
                            self.coverage[point].add(nums[0])
                        else:
                            self.coverage[point] = {nums[0]}

    def calc_overlapping_area(self) -> int:
        """
        Calculate the total area covered by one or more squares.
        """
        return len([1 for x in self.coverage.values() if len(x) >= 2])

    def find_non_overlaping(self) -> list[int]:
        """
        Get a list of the pieces of fabric that don't overlap woth any other.
        """
        all_fabrics = set()
        overlap_fabrics = set()

        # Determine the fabrics and those that overlap
        for overlap in self.coverage.values():
            all_fabrics.update(overlap)

            if len(overlap) > 1:
                overlap_fabrics.update(overlap)

        return [x for x in all_fabrics if x not in overlap_fabrics]


if __name__ == "__main__":
    elves = FabricSlicer("./data/input_0.txt")
    print(
        f"Part 1 = {elves.calc_overlapping_area()}\n"
        f"Part 2 = {elves.find_non_overlaping()}\n"
    )
