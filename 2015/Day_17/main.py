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


def read_container_sizes(file_path: str) -> list[int]:
    """
    Read the container sizes and return a list of integer sizes.
    """
    pass


def valid_cont_comb(eggnog: int, containers: list[int]) -> bool:
    """
    Determine if a certain set of `containers` can exactly fit all the `eggnog`.
    """
    pass


def find_poss_combs(eggnog: int, containers: list[int]) -> int:
    """
    Count the total number of combinations of `containers` that can
    completely fit all of supplied `eggnog`.
    """
    pass


if __name__ == "__main__":
    pass
