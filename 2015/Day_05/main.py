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
"""

VOWELS = "aeiou"
BAD_PATS = {"b": "ab", "d": "cd", "q": "pq", "y": "xy"}


def is_nice(test: str) -> bool:
    """
    Determine if the test string is nice. Done via three tests:
        * At least three vowels.
        * At least one douple letter next to itself.
        * No bad letter patterns.
    """

    double = False
    vowel_cnt = 0

    for idx, char in enumerate(test):

        # Check for the presence of a vowel
        if char in VOWELS:
            vowel_cnt += 1

        # These checks use the previous letter
        if idx != 0:

            # Check for a duplicate letter
            if test[idx] == test[idx - 1]:
                double = True

            # Ensure there no forbidden substrings
            if char in BAD_PATS and test[idx - 1 : idx + 1] == BAD_PATS[char]:
                return False

    return vowel_cnt >= 3 and double


def count_nice_strings(filepath: str) -> int:
    """
    Count the number of lines in a file which are nice strings.
    """
    nice_count = 0

    with open(filepath) as fp:
        for cand in fp.readlines():

            if is_nice(cand):
                nice_count += 1

    return nice_count


if __name__ == "__main__":
    print(f"The answer to part 1 = {count_nice_strings('./data/input.txt')}")
