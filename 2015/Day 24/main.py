"""
--- Day 24: It Hangs in the Balance ---

The packages need to be split into three groups of exactly the same weight, and
every package has to fit. The first group goes in the passenger compartment of
the sleigh, and the second and third go in containers on either side.

The first group - the one going in the passenger compartment - needs as few
packages as possible.

Furthermore, Santa tells you, if there are multiple ways to arrange the
packages such that the fewest possible are in the first group, you need to
choose the way where the first group has the smallest quantum entanglement to
reduce the chance of any "complications". The quantum entanglement of a group
of packages is the product of their weights, that is, the value you get when
you multiply their weights together. Only consider quantum entanglement if the
first group has the fewest possible number of packages in it and all groups
weigh the same amount.
"""

from itertools import product, combinations
import random

sample_weights = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
input_weights = [1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61,
                 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

# Create the different combinations of the weights in three groups

# What are the different combinations of the group sizes possible


def possible_group_sizes(number_of_weights, number_of_groups):
    """Generator to give the possible group sizes."""

    # Get all feasible and non-feasible group sizes
    possible_groups = product([x_w for x_w in range(1, number_of_weights)],
                              repeat=number_of_groups)

    for group in possible_groups:
        if sum(group) == number_of_weights:
            yield group
        else:
            continue


def generate_groups(group_size, weight_permutation):
    """Generate tuples of the group weights"""

    if len(weight_permutation) != sum(group_size):
        raise Exception("Group size and weights must match.")

    ret_ls = []

    for i in range(len(group_size)):

        if i == 0:
            ret_ls.append(weight_permutation[:group_size[i]])

        elif i == len(group_size) - 1:
            ret_ls.append(weight_permutation[-group_size[i]:])

        else:
            ret_ls.append(weight_permutation[
                          sum(group_split[:i]): sum(group_split[:i+1])])

    return tuple(ret_ls)


def equal_weights(weight_group) -> bool:
    """Work out if the weights in all three groups are the same"""

    sum_group_weights = [sum(x) for x in weight_group]

    if len(set(sum_group_weights)) != 1:
        return False
    else:
        return True


def quantum_entanglement(weight_group, qe_group=0) -> int:
    """Calculate the quantum entanglement of a package group"""

    prod = 1

    for num in weight_group[qe_group]:

        prod *= num

    return prod


# qe_results = []
#
# # Generate all the possible permutations of the weight array
# for weight_perm in permutations(input_weights):
#     for group_split in possible_group_sizes(len(input_weights), 3):
#
#         # Generate the group
#         tmp_group = generate_groups(group_split, weight_perm)
#
#         # Check the group has equal weights
#         if not equal_weights(tmp_group):
#             continue
#         else:
#             qe_results.append(quantum_entanglement(tmp_group))
#             print(quantum_entanglement(tmp_group),tmp_group)
#
# print(min(qe_results))


# For each possible group split
# for group_split in possible_group_sizes(len(input_weights), 3):
#
#     print(group_split)

for i in range(len(input_weights)):

    for comb in combinations(input_weights, i):

        print(comb)

