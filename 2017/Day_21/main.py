"""
--- Day 21: Fractal Art ---

You find a program trying to generate some art. It uses a strange process that
involves repeatedly enhancing the detail of an image through a set of rules.

The image consists of a two-dimensional square grid of pixels that are either
on (#) or off (.). The program always begins with this pattern:

.#.
..#
###

Because the pattern is both 3 pixels wide and 3 pixels tall, it is said to have
a size of 3.

Then, the program repeats the following process:

        -   If the size is evenly divisible by 2, break the pixels up into 2x2
            squares, and convert each 2x2 square into a 3x3 square by following
            the corresponding enhancement rule.

        -   Otherwise, the size is evenly divisible by 3; break the pixels up
            into 3x3 squares, and convert each 3x3 square into a 4x4 square by
            following the corresponding enhancement rule.

Because each square of pixels is replaced by a larger one, the image gains
pixels and so its size increases.

The artist's book of enhancement rules is nearby (your puzzle input); however,
it seems to be missing rules. The artist explains that sometimes, one must
rotate or flip the input pattern to find a match. (Never rotate or flip the
output pattern, though.) Each pattern is written concisely: rows are listed as
single units, ordered top-down, and separated by slashes. For example, the
following rules correspond to the adjacent patterns:

    ../.#  =  ..
            .#

                    .#.
    .#./..#/###  =  ..#
                    ###

                            #..#
    #..#/..../#..#/.##.  =  ....
                            #..#
                            .##.

When searching for a rule to use, rotate and flip the pattern as necessary. For
example, all of the following patterns match the same rule:

    .#.   .#.   #..   ###
    ..#   #..   #.#   ..#
    ###   ###   ##.   .#.

Suppose the book contained the following two rules:

    ../.# => ##./#../...
    .#./..#/### => #..#/..../..../#..#

As before, the program begins with this pattern:

    .#.
    ..#
    ###

The size of the grid (3) is not divisible by 2, but it is divisible by 3. It
divides evenly into a single square; the square matches the second rule, which
produces:

    #..#
    ....
    ....
    #..#

The size of this enhanced grid (4) is evenly divisible by 2, so that rule is
used. It divides evenly into four squares:

    #.|.#
    ..|..
    --+--
    ..|..
    #.|.#

Each of these squares matches the same rule (../.# => ##./#../...), three of
which require some flipping and rotation to line up with the rule. The output
for the rule is the same in all four cases:

    ##.|##.
    #..|#..
    ...|...
    ---+---
    ##.|##.
    #..|#..
    ...|...

Finally, the squares are joined into a new grid:

    ##.##.
    #..#..
    ......
    ##.##.
    #..#..
    ......

Thus, after 2 iterations, the grid contains 12 pixels that are on.

PART 1: How many pixels stay on after 5 iterations?

PART 2: How many pixels stay on after 18 iterations?
"""

import numpy as np


class FractalArt:
    def __init__(self, rule_file: str):
        self.pixels = np.array(
            [[False, True, False], [False, False, True], [True, True, True]], dtype=bool
        )

        # Read the instruction file and parse the instructions
        self.rules = []
        with open(rule_file, "r") as fp:
            for line in fp.readlines():
                line = line.replace("#", "1")
                line = line.replace(".", "0")
                line = line.replace("/", "")

                before, after = line.split(" => ", maxsplit=1)

                # Create 1D boolean arrays
                before = np.array(np.array(list(before.strip()), dtype=int), dtype=bool)
                after = np.array(np.array(list(after.strip()), dtype=int), dtype=bool)

                # Create Square arrays
                b_size = int(np.sqrt(len(before)))
                a_size = int(np.sqrt(len(after)))
                before = before.reshape((b_size, b_size))
                after = after.reshape((a_size, a_size))

                # Create the four rotated forms of the rotated before and the
                # flipped versions
                self.rules.extend(
                    [
                        [np.rot90(before, k=0), after],
                        [np.rot90(before, k=1), after],
                        [np.rot90(before, k=2), after],
                        [np.rot90(before, k=3), after],
                        [np.fliplr(before), after],
                        [np.flipud(before), after],
                        [np.fliplr(np.rot90(before, k=0)), after],
                        [np.fliplr(np.rot90(before, k=1)), after],
                        [np.fliplr(np.rot90(before, k=2)), after],
                        [np.fliplr(np.rot90(before, k=3)), after],
                        [np.flipud(np.rot90(before, k=0)), after],
                        [np.flipud(np.rot90(before, k=1)), after],
                        [np.flipud(np.rot90(before, k=2)), after],
                        [np.flipud(np.rot90(before, k=3)), after],
                    ]
                )

    def print_pixels(self, p_pixels: np.array) -> str:
        """
        Show a square grid of pixels.
        """
        art = ""

        for x in range(0, p_pixels.shape[0]):
            for y in range(0, p_pixels.shape[0]):
                if p_pixels[x, y]:
                    art += "#"
                else:
                    art += "."
            art += "\n"

        return art

    def show_rules(self):
        """
        Show the rules that are in the class
        """
        for before, after in self.rules:
            print(
                "BEFORE\n======\n"
                + self.print_pixels(before)
                + "AFTER\n=====\n"
                + self.print_pixels(after),
                end="\n\n",
            )

    def splits(self, num_splits: int):
        """
        Split the artwork into chunks of two or three and replace these chunks
        based on the rules inherent to the class.
        """
        for _ in range(num_splits):
            if self.pixels.shape[0] % 2 == 0:
                self.div_n_split(2)
            elif self.pixels.shape[0] % 3 == 0:
                self.div_n_split(3)
            else:
                raise Exceptions(f"Cannot process shape {self.pixels.shape}")

    def div_n_split(self, n: int):
        """
        Split the artwork into chunks of two and replace them according to the
        rules inherent to the class.
        """
        new_side_len = (self.pixels.shape[0] // n) * (n + 1)
        new_pixels = np.ones((new_side_len, new_side_len), dtype=bool)

        # Check each chunk for corresponding one in the rules
        for x in range(self.pixels.shape[0] // n):
            for y in range(self.pixels.shape[0] // n):
                chunk = self.pixels[x * n : x * n + n, y * n : y * n + n]

                # Find a match in the rules and set the new chunk
                for before, after in self.rules:
                    if chunk.shape == before.shape and np.all(chunk == before):
                        new_pixels[
                            x * (n + 1) : x * (n + 1) + (n + 1),
                            y * (n + 1) : y * (n + 1) + (n + 1),
                        ] = after
                        break
                else:
                    raise Exception(
                        f"No Match found for chunk:\n{self.print_pixels(chunk)}"
                    )

        # Set the new pixels
        self.pixels = new_pixels

    def count_on_pixels(self) -> int:
        """
        How many pixels in the artwork are True.
        """
        return np.sum(self.pixels)

    def __str__(self):
        self.print_pixels(self.pixels)


if __name__ == "__main__":
    basic_gen = FractalArt("./data/input.txt")
    basic_gen.splits(5)
    print(f"Part 1 = {basic_gen.count_on_pixels()}")
    basic_gen.splits(13)
    print(f"Part 2 = {basic_gen.count_on_pixels()}")
