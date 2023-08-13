"""
--- Day 7: The Treachery of Whales ---

A giant whale has decided your submarine is its next meal, and it's much faster
than you are. There's nowhere to run!

Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for
them otherwise) zooms in to rescue you! They seem to be preparing to blast a
hole in the ocean floor; sensors indicate a massive underground cave system
just beyond where they're aiming!

The crab submarines all need to be aligned before they'll have enough power to
blast a large enough hole for your submarine to get through. However, it doesn't
look like they'll be aligned before the whale catches you! Maybe you can help?

There's one major catch - crab submarines can only move horizontally.

You quickly make a list of the horizontal position of each crab (your puzzle
input). Crab submarines have limited fuel, so you need to find a way to make
all of their horizontal positions match while requiring them to spend as little
fuel as possible.

Part 1:
    Determine the horizontal position that the crabs can align to using the
    least fuel possible. How much fuel must they spend to align to that
    position?

Part 2:
    As it turns out, crab submarine engines don't burn fuel at a constant rate.
    Instead, each change of 1 step in horizontal position costs 1 more unit of
    fuel than the last: the first step costs 1, the second step costs 2, the
    third step costs 3, and so on.How much fuel must they spend to align to
    that position?
"""

import numpy as np

# Load the crab submarine data into memory
crab_sub_pos = [
    int(x) for x in open("./data/input.txt", "r").read().split(",")]

crab_sub_pos = np.array(crab_sub_pos)

scalar_move_costs = []
geometric_move_costs = []

# Iterate over all possible positions that the crabs could be move to
for dist in range(max(crab_sub_pos)):

    # Calculate the scaler crab move
    scale_move = np.abs(np.subtract(crab_sub_pos, dist))

    # Calculate the geometric crab move
    geom_move = (scale_move**2 + scale_move)/2

    # Save the total movement cost of all crabs
    scalar_move_costs.append(np.sum(scale_move))
    geometric_move_costs.append(np.sum(geom_move))

print(f"The answer to part one is: {min(scalar_move_costs)}")
print(f"The answer to part two is: {int(min(geometric_move_costs))}")
