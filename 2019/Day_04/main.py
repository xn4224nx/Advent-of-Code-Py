"""
--- Day 4: Secure Container ---

You arrive at the Venus fuel depot only to discover it's protected by a
password. The Elves had written the password on a sticky note, but someone threw
it out.

However, they do remember a few key facts about the password:

    -   It is a six-digit number.

    -   The value is within the range given in your puzzle input.

    -   Two adjacent digits are the same (like 22 in 122345).

    -   Going from left to right, the digits never decrease; they only ever
        increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    -   111111 meets these criteria (double 11, never decreases).

    -   223450 does not meet these criteria (decreasing pair of digits 50).

    -   123789 does not meet these criteria (no double).

PART 1: How many different passwords within the range given in your puzzle
        input meet these criteria?

An Elf just remembered one more important detail: the two adjacent matching
digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the
following are now true:

    -   112233 meets these criteria because the digits never decrease and all
        repeated digits are exactly two digits long.

    -   123444 no longer meets the criteria (the repeated 44 is part of a larger
        group of 444).

    -   111122 meets the criteria (even though 1 is repeated more than twice, it
        still contains a double 22).

PART 2: How many different passwords within the range given in your puzzle input
        meet all of the criteria?
"""


def valid_password(sec_num: int, single_double: bool = False) -> bool:
    """
    Apply rules to determine if this number could be a valid password.
    """
    num = str(sec_num)
    adj_digits = False

    for idx in range(1, len(num)):

        # Going from left to right, ensure the digits never decrease
        if ord(num[idx - 1]) > ord(num[idx]):
            return False

        # Detect a pair of identical numbers
        if num[idx] == num[idx - 1]:

            # Check the number before this pair
            if single_double and idx > 1 and num[idx - 2] == num[idx - 1]:
                continue

            # Check the number after this pair
            if single_double and idx < len(num) - 1 and num[idx + 1] == num[idx]:
                continue

            adj_digits = True

    return adj_digits


if __name__ == "__main__":
    print(
        f"Part 1 = {sum([valid_password(x) for x in range(254032, 789860)])}\n"
        f"Part 2 = {sum([valid_password(x, True) for x in range(254032, 789860)])}\n"
    )
