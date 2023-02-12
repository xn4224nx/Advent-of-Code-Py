"""
--- Day 2: Corruption Checksum ---

You need to calculate the spreadsheet's checksum. For each row, determine the
difference between the largest value and the smallest value; the checksum is
the sum of all of these differences.

"""

from itertools import combinations


def read_spread(fp: str) -> list[list[int]]:
    """Read a spreadsheet of integers."""

    # Load file into memory
    data = open(fp).read().splitlines()

    # For each row split by white space into its own list of ints
    data = [[int(x) for x in y.split()] for y in data]

    return data


def spread_checksum(spreadsheet: list[list[int]], check_type: str) -> int:
    """Calculate the checksum for a spreadsheet."""

    checksum = 0

    for row in spreadsheet:

        if check_type == "diff":

            # Find the largest & smallest value in each row
            checksum += max(row) - min(row)

        elif check_type == "div":
            for comb in combinations(row, 2):

                # In each row find the two numbers that are evenly divisible.
                if max(comb) % min(comb) == 0:
                    checksum += max(comb) // min(comb)
                    break

        else:
            raise Exception(f"{check_type} is not a supported checksum type.")

    return checksum


if __name__ == '__main__':

    spread = read_spread("data/input.txt")

    # Part 1
    print(spread_checksum(spread, "diff"))

    # Part 2
    print(spread_checksum(spread, "div"))
