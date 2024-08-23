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

Uh oh - the Accounting-Elves have realized that they double-counted everything
red.

Ignore any object (and all of its children) which has any property with the
value "red". Do this only for objects ({...}), not arrays ([...]).

PART 2: What is the sum of all numbers in the document if you ignore any object
        (and all of its children) that has the property red?
"""

import re
import json


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


def non_red_sum(storage) -> int:
    """
    Sum all numbers but ignore any object (and all of its children) which has
    any property with the value "red". Do this only for objects ({...}), not
    arrays ([...]).
    """
    if isinstance(storage, dict):
        if any(val == "red" for val in storage.values()):
            return 0

        total = 0
        for val in storage.values():
            total += non_red_sum(val)
        return total

    if isinstance(storage, list):
        return sum(non_red_sum(x) for x in storage)

    if isinstance(storage, int):
        return storage

    return 0


if __name__ == "__main__":
    raw_accounts = read_data("./data/input.txt")
    print(f"Part 1 = {sum_all_nums(raw_accounts)}")
    print(f"Part 2 = {non_red_sum(json.loads(raw_accounts))}")
