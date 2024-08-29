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

While playing with all the containers in the kitchen, another load of eggnog
arrives! The shipping and receiving department is requesting as many containers
as you can spare.

In the example above, the minimum number of containers was two. There were three
ways to use that many containers, and so the answer there would be 3.

PART 2: Find the minimum number of containers that can exactly fit all 150 liters
        of eggnog. How many different ways can you fill that number of containers
        and still hold exactly 150 litres?
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


def find_poss_combs(eggnog: int, containers: list[int], min_num: bool = False) -> int:
    """
    Count the total number of combinations of `containers` that can
    completely fit all of supplied `eggnog`.
    """
    pos_combs_size = {}

    # For each possible number of containers
    for num_conts in range(1, len(containers) + 1):

        # For each possible combination of containers of that number
        for cont_comb in itertools.combinations(containers, num_conts):

            # Can it fit the eggnog exactly
            if valid_cont_comb(eggnog, cont_comb):

                # Record the number of valid combinations for each number
                if num_conts not in pos_combs_size:
                    pos_combs_size[num_conts] = 0

                pos_combs_size[num_conts] += 1

    if not min_num:
        return sum([x for x in pos_combs_size.values()])

    else:
        min_cont_num = min([x for x in pos_combs_size.keys()])
        return sum([x for y, x in pos_combs_size.items() if y == min_cont_num])


if __name__ == "__main__":
    data = read_container_sizes("./data/input.txt")
    print(f"Part 1 = {find_poss_combs(150, data)}")
    print(f"Part 1 = {find_poss_combs(150, data, True)}")
