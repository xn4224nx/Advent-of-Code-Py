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

Part 2:
    If you can calculate the exact moments when the octopuses will all flash
    simultaneously, you should be able to navigate through the cavern. What is
    the first step during which all octopuses flash?
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


def single_flash_iter(energy_grid: np.array) -> int:
    """
    Have one iteration of the octopuses gaining energy and flashing. The
    function will return the new energy grid and the number of flashes in this
    step.
    """

    # Increase the energy level of each octopus
    energy_grid += 1
    flash_idx = []

    # Keep iterating if there are octopuses that are ready to flash
    while 10 in energy_grid:

        # Find the indexes of octopuses that will flash
        tmp_flash_idx = np.where(energy_grid == 10)

        # Iterate over the indexes and increase the energy levels of octopuses
        # near one that flashes
        for x_idx, y_idx in zip(tmp_flash_idx[0], tmp_flash_idx[1]):

            # Save the location of the flashes
            flash_idx.append((x_idx, y_idx))

            if x_idx == 0:
                x_effect = [x_idx, x_idx+1]

            elif x_idx == oct_energy.shape[0]-1:
                x_effect = [x_idx-1, x_idx]

            else:
                x_effect = [x_idx-1, x_idx, x_idx+1]

            if y_idx == 0:
                y_effect = [y_idx, y_idx + 1]

            elif y_idx == oct_energy.shape[1]-1:
                y_effect = [y_idx - 1, y_idx]

            else:
                y_effect = [y_idx - 1, y_idx, y_idx + 1]

            # Increase the energy of octopus around those who flash
            effected_idx = [(x, y) for x in x_effect for y in y_effect]
            energy_grid[tuple(zip(*effected_idx))] += 1

            # Deduplicate the flash index
            flash_idx = list(set(flash_idx))

            # Set all octopus who flash to zero energy
            energy_grid[tuple(zip(*flash_idx))] = 0

            # Set all octopus with >10 to 10 energy
            energy_grid[energy_grid > 10] = 10

    return len(flash_idx)


# Load the data
oct_energy = load_oct_energy_data("./data/input.txt")
flashes = 0

for i in range(100):
    flashes += single_flash_iter(oct_energy)

print(f"Part 1: {flashes}")
