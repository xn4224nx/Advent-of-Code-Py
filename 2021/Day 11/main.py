"""
--- Day 11: Dumbo Octopus ---

Each octopus has an energy level - your submarine can remotely measure the
energy level of each octopus (your puzzle input).

The energy level of each octopus is a value between 0 and 9.

You can model the energy levels and flashes of light in steps. During a single
step, the following occurs:

    First, the energy level of each octopus increases by 1.

    Then, any octopus with an energy level greater than 9 flashes. This
    increases the energy level of all adjacent octopuses by 1, including
    octopuses that are diagonally adjacent. If this causes an octopus to have
    an energy level greater than 9, it also flashes. This process continues as
    long as new octopuses keep having their energy level increased beyond 9.
    (An octopus can only flash at most once per step.)

    Finally, any octopus that flashed during this step has its energy level set
    to 0, as it used all of its energy to flash.

Part 1:
    Given the starting energy levels of the dumbo octopuses in your cavern,
    simulate 100 steps. How many total flashes are there after 100 steps?
"""

import numpy as np


def load_oct_energy_data(filename: str) -> np.array:
    """
    Load the octopuses energy data from file and return a numpy array.
    """

    raw_oct_energy = open(filename, "r").read().splitlines()

    # Parse the energy values
    raw_oct_energy = np.array([[int(x) for x in y] for y in raw_oct_energy])

    return raw_oct_energy


# Load the data
oct_energy = load_oct_energy_data("./data/sample.txt")

print(oct_energy)
