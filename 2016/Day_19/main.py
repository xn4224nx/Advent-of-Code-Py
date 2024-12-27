"""
--- Day 19: An Elephant Named Joseph ---

The Elves contact you over a highly secure emergency channel. Back at the North
Pole, the Elves are busy misunderstanding White Elephant parties.

Each Elf brings a present. They all sit in a circle, numbered starting with
position 1. Then, starting with the first Elf, they take turns stealing all the
presents from the Elf to their left. An Elf with no presents is removed from the
circle and does not take turns.

Each Elf brings a present. They all sit in a circle, numbered starting with
position 1. Then, starting with the first Elf, they take turns stealing all the
presents from the Elf to their left. An Elf with no presents is removed from the
circle and does not take turns.

For example, with five Elves (numbered 1 to 5):

  1
5   2
 4 3

    -   Elf 1 takes Elf 2's present.
    -   Elf 2 has no presents and is skipped.
    -   Elf 3 takes Elf 4's present.
    -   Elf 4 has no presents and is also skipped.
    -   Elf 5 takes Elf 1's two presents.
    -   Neither Elf 1 nor Elf 2 have any presents, so both are skipped.
    -   Elf 3 takes Elf 5's three presents.

So, with five Elves, the Elf that sits starting in position 3 gets all the
presents.

PART 1: With the number of Elves given in your puzzle input, which Elf gets all
        the presents?

Realizing the folly of their present-exchange rules, the Elves agree to instead
steal presents from the Elf directly across the circle. If two Elves are across
the circle, the one on the left (from the perspective of the stealer) is stolen
from. The other rules remain unchanged: Elves with no presents are removed from
the circle entirely, and the other elves move in slightly to keep the circle
evenly spaced.

PART 2: With the number of Elves given in your puzzle input, which Elf now gets
        all the presents?
"""

from math import log


def find_final_elf(num_elves: int) -> int:
    """
    Determine the number of the elf that gets all the presents in the white
    elephant party using the Josephus problem.
    """

    # Convert to binary
    num = bin(num_elves)[2:]

    # Extract the most significant bit and append the bit as the least significant bit
    num = "0b" + num[1:] + num[0]

    # Convert back to base 10
    return int(num, 2)


def find_final_elf_half(num_elves: int) -> int:
    """
    A white elephant party where the Elf the otherside of the current one gets
    all their presents stolen.
    """
    p = 3 ** int(log(num_elves - 1, 3))
    return num_elves - p + max(num_elves - 2 * p, 0)


if __name__ == "__main__":
    print(f"Part 1 = {find_final_elf(3018458)}")
    print(f"Part 2 = {find_final_elf_half(3018458)}")
