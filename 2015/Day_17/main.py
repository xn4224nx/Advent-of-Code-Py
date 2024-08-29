"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all into
your refrigerator, you'll need to move it into smaller containers. You take an
inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If
you need to store 25 liters, there are four ways to do it:

    - 15 and 10
    - 20 and 5 (the first 5)
    - 20 and 5 (the second 5)
    - 15, 5, and 5

PART 1: Filling all containers entirely, how many different combinations of
        containers can exactly fit all 150 liters of eggnog?
"""

import itertools


def read_container_sizes(file_path: str) -> list[int]:
    """
    Read the container sizes and return a list of integer sizes.
    """
    with open(file_path) as fp:
        return [int(x) for x in fp.readlines()]


def valid_cont_comb(eggnog: int, containers: list[int]) -> bool:
    """
    Determine if a certain set of `containers` can exactly fit all the `eggnog`.
    """
    return sum(containers) == eggnog


def find_poss_combs(eggnog: int, containers: list[int]) -> int:
    """
    Count the total number of combinations of `containers` that can
    completely fit all of supplied `eggnog`.
    """
    num_pos_combs = 0

    for num_conts in range(1, len(containers) + 1):
        for cont_comb in itertools.combinations(containers, num_conts):
            if valid_cont_comb(eggnog, cont_comb):
                num_pos_combs += 1

    return num_pos_combs


if __name__ == "__main__":
    data = read_container_sizes("./data/input.txt")
    print(f"Part 1 = {find_poss_combs(150, data)}")
