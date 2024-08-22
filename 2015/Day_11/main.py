"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has
devised a method of coming up with a password based on the previous one.
Corporate policy dictates that passwords must be exactly eight lowercase letters
(for security reasons), so he finds his new password by incrementing his old
password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on.
Increase the rightmost letter one step; if it was z, it wraps around to a, and
repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed
some additional password requirements:

    *   Passwords must include one increasing straight of at least three
        letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip
        letters; abd doesn't count.

    *   Passwords may not contain the letters i, o, or l, as these letters can
        be mistaken for other characters and are therefore confusing.

    *   Passwords must contain at least two different, non-overlapping pairs of
        letters, like aa, bb, or zz.

PART 1: Given Santa's current password (your puzzle input), what should his next
        password be?
"""


def increment_string(value: str) -> str:
    """
    Change a string moving a -> z one column at a time one char at a time.
    """
    new = ""
    incr = True
    value = value[::-1]

    for idx in range(len(value)):
        if incr:
            if value[idx] == "z":
                new += "a"
            else:
                new += chr(ord(value[idx]) + 1)
                incr = False
        else:
            new += value[idx]

        idx -= 1

    return new[::-1]


def valid_password(password: str) -> bool:
    """
    Assertain if a password passes all the rules for the new Security-Elf.
    """
    inc_chars = False
    char_pairs = set()
    skip_check = False

    for idx in range(1, len(password)):
        if password[idx] in ["i", "o", "l"]:
            return False

        if not skip_check and password[idx] == password[idx - 1]:
            char_pairs.add(password[idx - 1 : idx + 1])
            skip_check = True
        else:
            skip_check = False

        # test for a triplet of increasing characters
        if idx > 1 and (
            ord(password[idx - 2]) + 2
            == ord(password[idx - 1]) + 1
            == ord(password[idx])
        ):
            inc_chars = True

    return inc_chars and len(char_pairs) >= 2


def find_next_pass(start: str) -> str:
    """
    Going from the starting password determine the next valid password.
    """
    while True:
        start = increment_string(start)
        if valid_password(start):
            return start

        if start == "".join("z" for _ in range(len(start))):
            return start


if __name__ == "__main__":
    print(f"Part 1 = {find_next_pass('hxbxwxba')}")
