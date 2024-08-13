"""
--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say. They
take turns making sequences by reading aloud the previous
sequence and using that reading as the next sequence. For
example, 211 is read as "one two, two ones", which becomes
1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the
previous value as input for the next step. For each step,
take the previous value, and replace each run of digits (like
111) with the number of digits (3) followed by the digit
itself (1).

PART 1: Starting with the digits in your puzzle input, apply
        this process 40 times. What is the length of the
        result?
"""

import itertools


def look_and_say(old_seq: str) -> str:
    """
    The original sequence is transformed using the rules of
    the look-and-say game
    """
    new_seq = ""

    for k, g in itertools.groupby(old_seq):
        new_seq += str(len(list(g)))
        new_seq += str(k)

    return new_seq


if __name__ == "__main__":
    start = "1113122113"

    for i in range(40):
        start = look_and_say(start)

    print(f"Part 1 answer = {len(start)}")
