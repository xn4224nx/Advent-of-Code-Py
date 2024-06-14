"""
--- Day 19: Medicine for Rudolph ---

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission
plant, capable of constructing any Red-Nosed Reindeer molecule you need. It
works by starting with some input molecule and then doing a series of
replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration
involves determining the number of molecules that can be generated in one step
from a given starting point.
"""

import re


def new_molecules(init_molecule, sub) -> list:
    """
    Find all the possible molecules that can be made from one substitution and
    the initial molecule
    """

    # Find all occurrences of the sub[0] in the initial molecule
    sub_idx = [i for i in range(len(init_molecule))
               if init_molecule.startswith(sub[0], i)]

    ret_ls = []

    # Replace one and only one instance of the sub[0] with sub[1] in the
    # initial molecule
    for idx in sub_idx:
        # Remove the substring from the initial molecule and put the
        # substitution in its place
        ret_ls.append(init_molecule[:idx] + sub[1] +
                      init_molecule[idx + len(sub[0]):])

    return ret_ls


def replacement_step(init_molecules, sub_arr) -> list:
    """
    Find out all the possible molecules that can be created from the array of
    initial molecules and the possible substitutions
    """

    possible_molecules = []

    for i_molecule in init_molecules:
        for sub in sub_arr:
            possible_molecules += new_molecules(i_molecule, sub)

    # Remove duplicates
    return list(set(possible_molecules))


def load_data(file) -> tuple:

    data = open(file).read().splitlines()

    sub_ls = []

    # Parse the substitutions
    for line in data:

        # Don't process beyond the instructions
        if line == '':
            break

        # Parse the molecule replacement text
        sub_ls.append(re.findall(r"([A-Za-z]+) => ([A-Za-z]+)", line)[0])

    return sub_ls, data[-1]


def replace_all(init_molecule, sub_arr) -> (str, int):
    """Make every replacement possible in the molecule"""

    # Record the total number of substitutions made
    sub_count = 0

    new_molecule = init_molecule

    # Fow each possible substitution
    for sub in sub_arr:

        if sub[0] in new_molecule:

            # Replace all occurrences
            sub_count += new_molecule.count(sub[0])
            new_molecule = new_molecule.replace(sub[0], sub[1])

    return new_molecule, sub_count


# Load the data
substitutions, molecule = load_data('data/input.txt')

# Invert the substitutions
inverse_sub_arr = [(sub[1], sub[0]) for sub in substitutions]

# Run one substitution step of steps
new = replacement_step([molecule], substitutions)

# reverse the substitutions to get to "e"
rev_molecule = molecule
total_subs = 0

# Make replacements
while rev_molecule != "e":
    rev_molecule, new_subs = replace_all(rev_molecule, inverse_sub_arr)
    total_subs += new_subs

# Part 1
print(len(new))

# Part 2
print(total_subs)

