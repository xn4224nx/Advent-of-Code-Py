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

from itertools import combinations_with_replacement, permutations


def read_box_sizes(file_path: str) -> list[int]:
    """
    From disk read the box sizes and return a list of them.
    """
    with open(file_path, "r") as fp:
        return [int(x) for x in fp.readlines()]


def calc_group_qe(group: list[int]) -> int:
    """
    Calculate the quantum entanglement score of a group of box sizes.
    """
    prod = 1
    for val in group:
        prod *= val

    return prod


def calc_group_weight(group: list[int]) -> int:
    """
    Determine the sum of the weights of the boxes in a group.
    """
    return sum(group)


def check_all_weights_same(multi_group: list[list[int]]) -> bool:
    """
    Confirm all the groups have the same weight.
    """
    group_weights = [calc_group_weight(x) for x in multi_group]
    return min(group_weights) == max(group_weights)


def check_first_group_fewest(multi_group: list[list[int]]) -> bool:
    """
    Ensure that the first group has the smallest number of boxes, or is drawn
    for lowest with other boxes.
    """
    for idx in range(1, len(multi_group)):
        if len(multi_group[idx]) < len(multi_group[0]):
            return False

    return True


def check_first_group_size_fewest(group_sizes: tuple[int]) -> bool:
    """
    Ensure that the first group size has the smallest number of boxes, or is
    drawn for lowest with other boxes.
    """
    for idx in range(1, len(group_sizes)):
        if group_sizes[idx] < group_sizes[0]:
            return False

    return True


def iter_over_group_combs(boxes: list[int], num_groups: int) -> list[list[int]]:
    """
    A generator to iterate over all the possible valid box group combinations.
    """
    # Iterate over the possible group sizes
    for group_sizes in combinations_with_replacement(
        [x for x in range(1, len(boxes))], num_groups
    ):

        # Every box needs to be able to fit into the groups exactly
        if sum(group_sizes) != len(boxes):
            continue

        # The first group needs to be smallest
        if not check_first_group_size_fewest(group_sizes):
            continue

        # Iterate over every permutation of the box ordering
        for shuf_boxes in permutations(boxes):
            conv_boxes = list(shuf_boxes)

            # Create the group of group of boxes
            box_comb = []
            for size in group_sizes:
                tmp = []
                for _ in range(size):
                    tmp.append(conv_boxes.pop())
                box_comb.append(tmp)

            # Test the validity
            if check_all_weights_same(box_comb):
                yield box_comb


def find_lowest_qe(boxes: list[int], num_groups: int) -> int:
    """
    Find the lowest quantum entanglement of all the valid box groups.
    """
    pass


if __name__ == "__main__":
    pass
