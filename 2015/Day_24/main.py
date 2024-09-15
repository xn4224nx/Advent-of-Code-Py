"""
--- Day 24: It Hangs in the Balance ---

It's Christmas Eve, and Santa is loading up the sleigh for this year's
deliveries. However, there's one small problem: he can't get the sleigh to
balance. If it isn't balanced, he can't defy physics, and nobody gets presents
this year.

No pressure.

Santa has provided you a list of the weights of every package he needs to fit
on the sleigh. The packages need to be split into three groups of exactly the
same weight, and every package has to fit. The first group goes in the
passenger compartment of the sleigh, and the second and third go in containers
on either side. Only when all three groups weigh exactly the same amount will
the sleigh be able to fly. Defying physics has rules, you know!

Of course, that's not the only problem. The first group - the one going in the
passenger compartment - needs as few packages as possible so that Santa has
some legroom left over. It doesn't matter how many packages are in either of
the other two groups, so long as all of the groups weigh the same.

Furthermore, Santa tells you, if there are multiple ways to arrange the
packages such that the fewest possible are in the first group, you need to
choose the way where the first group has the smallest quantum entanglement to
reduce the chance of any "complications". The quantum entanglement of a group
of packages is the product of their weights, that is, the value you get when
you multiply their weights together. Only consider quantum entanglement if the
first group has the fewest possible number of packages in it and all groups
weigh the same amount.

PART 1: What is the quantum entanglement of the first group of packages in the
        ideal configuration?
"""


def read_box_sizes(file_path: str) -> list[int]:
    """
    From disk read the box sizes and return a list of them.
    """
    pass


def calc_group_qe(group: list[int]) -> int:
    """
    Calculate the quantum entanglement score of a group of box sizes.
    """
    pass


def calc_group_weight(group: list[int]) -> int:
    """
    Determine the sum of the weights of the boxes in a group.
    """
    pass


def check_all_weights_same(multi_group: list[list[int]]) -> bool:
    """
    Confirm all the groups have the same weight.
    """
    pass


def check_first_group_fewest(multi_group: list[list[int]]) -> bool:
    """
    Ensure that the first group has the smallest number of boxes, or is drawn
    for lowest with other boxes.
    """
    pass


def iter_over_group_combs(group_sizes: list[int], num_groups: int) -> list[list[int]]:
    """
    A generator to iterate over all the possible valid box group combinations.
    """
    pass


def find_lowest_qe(group_sizes: list[int]) -> int:
    """
    Find the lowest quantum entanglement of all the valid box groups.
    """
    pass


if __name__ == "__main__":
    pass
