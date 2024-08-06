"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are
naughty or nice.

A nice string is one with all of the following properties:

    1)  It contains at least three vowels (aeiou only), like aei,
        xazegov, or aeiouaeiouaeiou.

    2)  It contains at least one letter that appears twice in a row,
        like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).

    3)  It does not contain the strings ab, cd, pq, or xy, even if
        they are part of one of the other requirements.

PART 1: How many strings are nice?

Realizing the error of his ways, Santa has switched to a better model of
determining whether a string is naughty or nice. None of the old rules apply,
as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    1)  It contains a pair of any two letters that appears at least twice in
        the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but
        not like aaa (aa, but it overlaps).

    2)  It contains at least one letter which repeats with exactly one letter
        between them, like xyx, abcdefeghi (efe), or even aaa.

PART 2: How many strings are nice under these new rules?
"""

from typing import Callable


def is_nice(test: str) -> bool:
    """
    Determine if the test string is nice. Done via three tests:
        * At least three vowels.
        * At least one douple letter next to itself.
        * No bad letter patterns.
    """
    bad_pairs = {"b": "ab", "d": "cd", "q": "pq", "y": "xy"}

    double = False
    vowel_cnt = 0

    for idx, char in enumerate(test):

        # Check for the presence of a vowel
        if char in "aeiou":
            vowel_cnt += 1

        # These checks use the previous letter
        if idx != 0:

            # Check for a duplicate letter
            if test[idx] == test[idx - 1]:
                double = True

            # Ensure there no forbidden substrings
            if char in bad_pairs and test[idx - 1 : idx + 1] == bad_pairs[char]:
                return False

    return vowel_cnt >= 3 and double


def is_nice_2(test: str) -> bool:
    """
    Determine if the test string is nice (2nd varient). This is determined by
    the two tests:

        *   It contains a pair of any two letters that appears at least twice
            in the string without overlapping.

        *   It contains at least one letter which repeats with exactly one
            letter between them.

    Both tests have to be passed for the string to be nice.
    """
    space_repeat = letter_pair = False

    for idx, char in enumerate(test):

        # Check for the repeated char seperated by another char
        if idx >= 2 and test[idx] == test[idx - 2]:
            space_repeat = True

        # Extract the pairs in the string
        if idx + 2 < len(test) and not letter_pair:

            # Extract the relevant pair
            t_slice = test[idx : idx + 2]

            # See if the pair is repeated in the rest of the string.
            for jdx in range(idx + 2, len(test) - 1):

                if test[jdx : jdx + 2] == t_slice:
                    letter_pair = True
                    break

        # If both conditions have been matched don't contiue checking
        if space_repeat and letter_pair:
            return True

    return False


def count_nice_strings(nice_test: Callable[str, [bool]], filepath: str) -> int:
    """
    Count the number of lines in a file which are nice strings. `nice_test` is a
    function that takes a string and determines if it is nice, indicated by a
    returned boolean.
    """
    nice_count = 0

    with open(filepath) as fp:
        for cand in fp.readlines():

            if nice_test(cand):
                nice_count += 1

    return nice_count


if __name__ == "__main__":
    print(f"The answer to part 1 = {count_nice_strings(is_nice, './data/input.txt')}")
    print(f"The answer to part 2 = {count_nice_strings(is_nice_2, './data/input.txt')}")
