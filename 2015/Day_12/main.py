"""
--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order.
Unfortunately, their accounting software uses a peculiar storage format. That's
where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]),
objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find
all of the numbers throughout the document and add them together.

You will not encounter any strings containing numbers.

PART 1: What is the sum of all numbers in the document?
"""

import re


def read_data(file_path: str) -> str:
    """
    Parse the data file into an array of strings.
    """
    with open(file_path) as fp:
        return fp.read()


def sum_all_nums(storage: str) -> int:
    """
    Collect all the numbers in the storage object and return the sum
    """
    return sum([int(x.group()) for x in re.finditer(r"-?\d+", storage)])


if __name__ == "__main__":
    raw_accounts = read_data("./data/input.txt")
    print(f"Part 1 = {sum_all_nums(raw_accounts)}")
