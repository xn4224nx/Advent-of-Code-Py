"""
--- Day 3: Binary Diagnostic ---

The diagnostic report (your puzzle input) consists of a list of binary numbers 
which, when decoded properly, can tell you many useful things about the 
conditions of the submarine. The first parameter to check is the power 
consumption.

You need to use the binary numbers in the diagnostic report to generate two new 
binary numbers (called the gamma rate and the epsilon rate). The power 
consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in 
the corresponding position of all numbers in the diagnostic report.

Part 1:

    Use the binary numbers in your diagnostic report to calculate the gamma rate
    and epsilon rate, then multiply them together. What is the power consumption
    of the submarine?

Part 2:

    Next, you should verify the life support rating, which can be determined by
    multiplying the oxygen generator rating by the CO2 scrubber rating.

"""

import numpy as np
from scipy.stats import mode


def modal_bit(bits: np.array, axis_b: int, check_draw=False) -> np.array:
    """
    Using a 2d array of ints find the modal along the axis.
    """

    # Find the most  and least common bit in each column
    modal_details = mode(bits, axis=axis_b)
    counts = modal_details.count
    modes = modal_details.mode

    # Get the most & least common values
    most_in_col = np.array(modes, dtype=bool)
    least_in_col = np.invert(most_in_col.copy())

    # Convert back to integer
    most_in_col = np.array(most_in_col, dtype=int)
    least_in_col = np.array(least_in_col, dtype=int)

    # Convert back to str
    most_in_col = np.array(most_in_col, dtype=str)
    least_in_col = np.array(least_in_col, dtype=str)

    if check_draw:
        half_len = int(bits.shape[0]/2)
        most_in_col[counts == half_len] = None
        least_in_col[counts == half_len] = None

    return most_in_col, least_in_col


def str_bin_to_int(arr: np.array) -> int:
    """
    Convert an array of 0s and 1s to the integer representation of the binary
    number.
    """

    # Convert to a string of 1s of 0s
    bin_ls = "".join([str(x) for x in arr])

    # Convert the string to an integer
    num = int(bin_ls, 2)

    return num


if __name__ == "__main__":

    # Load the text file and split into substrings
    diag = open("./data/input.txt", "r").read().splitlines()
    diag = [list(x) for x in diag]

    # Convert to a numpy array
    diagnostics = np.array(diag, dtype=int)

    # Find the most  and least common bit in each column
    most_com, least_com = modal_bit(diagnostics, 0)

    # Convert the list of bits to an integer
    gamma = str_bin_to_int(most_com)
    epsilon = str_bin_to_int(least_com)

    # Show the answer to part 1
    print(f"Part 1: The power consumption of the sub = {gamma * epsilon}")

    # Make a copy of the diagnostics for oxygen and the scrubbers
    diag_o = diagnostics.copy()
    diag_s = diagnostics.copy()

    # For each bit position in the diagnostic message
    for bit_idx in range(len(diag[0])):

        if diag_s.shape[0] > 1:

            # Find the most  and least common bit in each column
            most_com_s, least_com_s = modal_bit(diag_s, 0, True)

            # Find the most & least common bit in the bit_idx position
            if least_com_s[bit_idx] == "None":
                pick_scu = 0
            else:
                pick_scu = int(least_com_s[bit_idx])

            diag_s = diag_s[diag_s[:, bit_idx] == pick_scu]

        if diag_o.shape[0] > 1:

            # Find the most  and least common bit in each column
            most_com_s, least_com_s = modal_bit(diag_o, 0, True)

            # Find the most & least common bit in the bit_idx position
            if most_com_s[bit_idx] == "None":
                pick_oxy = 1
            else:
                pick_oxy = int(most_com_s[bit_idx])

            diag_o = diag_o[diag_o[:, bit_idx] == pick_oxy]

    scrubber = str_bin_to_int(diag_s[0])
    oxygen = str_bin_to_int(diag_o[0])

    print(f"Part 2: The life support rating of the sub = {scrubber * oxygen}")
