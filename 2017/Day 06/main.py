"""
--- Day 6: Memory Reallocation ---

In this area, there are sixteen memory banks; each memory bank can hold any
number of blocks. The goal of the reallocation routine is to balance the blocks
between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory
bank with the most blocks (ties won by the lowest-numbered memory bank) and
redistributes those blocks among the banks.

To do this, it removes all the blocks from the selected bank, then moves to
the next (by index) memory bank and inserts one of the blocks. It continues
doing this until it runs out of blocks; if it reaches the last memory bank, it
wraps around to the first one.


Part 1

The debugger would like to know how many redistributions can be done before a
blocks-in-banks configuration is produced that has been seen before.


Part 2

Out of curiosity, the debugger would also like to know the size of the loop:
starting from a state that has already been seen, how many block redistribution
cycles must be performed before that same state is seen again?

"""

import numpy as np


def load_mem_banks(fp: str) -> np.array:
    """Load the memory sizes from text files."""

    data = open(fp, "r").read().split()
    data = [int(x) for x in data]

    return np.array(data)


def next_idx_in_cycle(arr_len: int, idx: int) -> int:
    """
    When cycling through a loop of an array what is the next index if it
    cycles back on itself?
    """

    if idx >= arr_len-1:
        idx = 0
    else:
        idx += 1

    return idx


def redist_mem_banks(mem_banks: np.array):
    """Redistribute the largest memory bank to the others."""

    cpy_banks = mem_banks.copy()

    # Find the memory bank with the largest number of blocks
    idx_largest_bank = np.argmax(cpy_banks)

    # Redistribute the blocks to the other banks from the next bank onward
    blocks_to_redistribute = cpy_banks[idx_largest_bank]
    cpy_banks[idx_largest_bank] = 0
    index = next_idx_in_cycle(len(cpy_banks), idx_largest_bank)

    while blocks_to_redistribute > 0:
        cpy_banks[index] += 1
        blocks_to_redistribute -= 1

        # Cycle over the array as long as there are blocks to distribute
        index = next_idx_in_cycle(len(cpy_banks), index)

    return cpy_banks


def str_membank_rep(mem_banks: np.array) -> str:
    """Creates a string form of a memeory bank configuration."""
    return np.array2string(mem_banks, separator="_")


def count_cycles_in_redistribution_loop(mem_banks: np.array):
    """
    Calculate the cycles it takes to redistribute back to a previously seen
    memory configuration.
    """

    prev_seen_distributions = {str_membank_rep(mem_banks): None}
    cycles = 1

    # Part 1
    while True:

        new_dist = redist_mem_banks(mem_banks)

        if str_membank_rep(new_dist) in prev_seen_distributions:
            first_repeat_config = new_dist
            print(cycles)
            break
        else:
            prev_seen_distributions[str_membank_rep(new_dist)] = None

        mem_banks = new_dist
        cycles += 1

    # Part 2
    repeat_cycles = 0
    while not np.array_equal(first_repeat_config, mem_banks):
        mem_banks = redist_mem_banks(new_dist)

        repeat_cycles += 1
        new_dist = mem_banks

    print(repeat_cycles)


memory_banks = load_mem_banks("data/input.txt")

# Part 1 & 2
count_cycles_in_redistribution_loop(memory_banks)
