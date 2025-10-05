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
"""


def valid_password(sec_num: int) -> bool:
    """
    Apply rules to determine if this number could be a valid password.
    """
    num = str(sec_num)
    adj_digits = False

    for digit_idx in range(1, len(num)):

        # At least two adjacent digits must be identical
        if not adj_digits and num[digit_idx] == num[digit_idx - 1]:
            adj_digits = True

        # Going from left to right, the digits never decrease
        if ord(num[digit_idx - 1]) > ord(num[digit_idx]):
            return False

    return adj_digits


if __name__ == "__main__":
    print(f"Part 1 = {sum([valid_password(x) for x in range(254032, 789860)])}")
