"""
--- Day 20: Infinite Elves and Infinite Houses ---

To keep the Elves busy, Santa has them deliver some presents by hand, door-to-
door. He sends them down a street with infinite houses numbered sequentially: 1,
2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on
that number:

    -   The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4,
        5, ....

    -   The second Elf (number 2) delivers presents to every second house: 2,
        4, 6, 8, 10, ....

    -   Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15,
        ....

There are infinitely many Elves, numbered starting with 1. Each Elf delivers
presents equal to ten times his or her number at each house.

PART 1: What is the lowest house number of the house to get at least as many
        presents as the number in your puzzle input?
"""

import numpy as np


def find_lowest_house(num_pres: int) -> int:
    """
    Find the lowest house number to get a certain number of presents.
    """
    num_houses = num_pres // 10

    # Allocate the houses to fill with presents.
    house_pres = np.zeros(num_houses)

    # Simulate the elves delivering presents
    for idx in range(1, num_houses):
        house_pres[idx::idx] += 10 * idx

    return np.where(house_pres >= num_pres)[0][0]


if __name__ == "__main__":
    print(f"Part 1 = {find_lowest_house(34000000)}")
