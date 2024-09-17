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

from itertools import combinations_with_replacement, combinations


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


def find_a_valid_group(
    cur_boxes: list[int], target_sum: int, max_grp_size: int
) -> tuple[int]:
    """
    Determine valid group compositions. Return the boxes in the valid group
    """
    for grp_size in range(1, max_grp_size):
        for comb in combinations(cur_boxes, grp_size):
            if sum(comb) == target_sum:
                yield comb


def find_valid_group_sizes(num_boxes: int, num_grps: int) -> list[tuple[int]]:
    """
    Determine the possible group sizes
    """
    # Iterate over the possible group sizes
    for group_sizes in combinations_with_replacement(
        [x for x in range(1, num_boxes)], num_grps
    ):
        # Every box needs to be able to fit into the groups exactly
        if sum(group_sizes) != num_boxes:
            continue

        # The first group needs to be smallest
        if not check_first_group_size_fewest(group_sizes):
            continue

        yield group_sizes


def find_lowest_qe_3grps(boxes: list[int]) -> int:
    """
    Determine the valid groups of boxes.
    """
    num_groups = 3

    group_sum = sum(boxes) / num_groups
    lowest_valid_first_group_size = len(boxes)
    results = []

    # Iterate over every possible size of the box groups
    for grp_sizes in find_valid_group_sizes(len(boxes), num_groups):

        if lowest_valid_first_group_size < grp_sizes[0]:
            break

        # Find valid ways to make the first group
        for grp_0 in combinations(boxes, grp_sizes[0]):

            # If it has the not got the right sum
            if sum(grp_0) != group_sum:
                continue

            # Work out the remaining boxes that are in the other groups
            rem_boxes_0 = [x for x in boxes if x not in grp_0]

            # Find valid ways to make the second group
            for grp_1 in combinations(rem_boxes_0, grp_sizes[1]):

                # If it has the not got the right sum
                if sum(grp_1) != group_sum:
                    continue

                # Work out the remaining boxes that are in the other groups
                rem_boxes_1 = [x for x in boxes if x not in grp_1]

                results.append(calc_group_qe(grp_0))
                lowest_valid_first_group_size = grp_sizes[0]

    return min(results)


if __name__ == "__main__":
    boxes = read_box_sizes("./data/input.txt")
    print(f"Part 1 = {find_lowest_qe_3grps(boxes)}")
