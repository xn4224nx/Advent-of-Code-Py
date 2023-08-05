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

Use the binary numbers in your diagnostic report to calculate the gamma rate and
epsilon rate, then multiply them together. What is the power consumption of the 
submarine?
"""


def str_char_freq(input_str: str) -> dict[str: int]:
    """
    Find the frequency of each char in a string.
    """
    freq = {}

    for char in input_str:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    return freq


def most_n_least_common(char_freq: dict[str: int]) -> (str, str):
    """
    Using a frequency dictionary find the least and most common chars.
    Return most common and least common in a tuple.
    """

    return (
        max(char_freq, key=char_freq.get),
        min(char_freq, key=char_freq.get)
    )


if __name__ == "__main__":

    # Load the data
    diag = open("./data/input.txt", "r").read().splitlines()

    # Create storage for the column of bits
    col_bits = ["" for x in range(len(diag[0]))]

    # Iterate over each line in the diagnostic file
    for line in diag:

        # Save each bit in the line to each column string
        for i in range(len(line)):
            col_bits[i] += line[i]

    # Calculate the Epsilon and Gamma
    epsilon = ""
    gamma = ""

    for col in col_bits:

        # Get the frequency of each char in the column
        char_freqs = str_char_freq(col)

        # get the epsilon and gamma
        gam, eps = most_n_least_common(char_freqs)

        # Add the characters to the gamma and epsilon
        epsilon += eps
        gamma += gam

    # Convert the strings to an integer then a binary
    epsilon = int(epsilon, 2)
    gamma = int(gamma, 2)

    print(f"Part 1: The power consumption of the sub = {gamma * epsilon}")
