"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a
passphrase instead of simply a password. A passphrase consists of a series of
words (lowercase letters) separated by spaces.

Part 1

To ensure security, a valid passphrase must contain no duplicate words.
How many passphrases are valid?

Part 2

Now, a valid passphrase must contain no two words that are anagrams of each
other - that is, a passphrase is invalid if any word's letters can be
rearranged to form any other word in the passphrase.

"""


def load_passwords(fp: str) -> list[list[str]]:
    """Load passwords from file and tokenise the lines."""

    # Load the data
    data = open(fp, "r").read().splitlines()

    # Split the lines into tokens
    data = [x.split() for x in data]

    return data


def detect_valid_pass(pass_ls: list[str]) -> bool:
    """Are there any duplicate stings in the pass phrase?"""

    num_words = len(pass_ls)

    num_unique = len(set(pass_ls))

    return num_words == num_unique


def str_2_letter_dict(pass_str: str) -> str:
    """Transform a string into a dict of the letter to its count in the str."""

    res_dict = {}

    for char in pass_str:
        if char in res_dict:
            res_dict[char] += 1
        else:
            res_dict[char] = 1

    # Create str representation of the dict
    ret_str = ""

    for char in sorted(res_dict):
        ret_str += str(char) + str(res_dict[char])

    return ret_str


def detect_anagram_pass(pass_ls: list[str]) -> bool:
    """Detect passphrases that are anagrams of each other."""

    # Transform the pass phrases into dict of letter counts
    pass_dicts = [str_2_letter_dict(x) for x in pass_ls]

    unique_dicts = set(pass_dicts)

    return len(pass_dicts) == len(unique_dicts)


input_pass = load_passwords("data/input.txt")

# Part 1
num_valid = [detect_valid_pass(x) for x in input_pass]
print(sum(num_valid))

# Part 2
num_valid_2 = [detect_anagram_pass(x) for x in input_pass]
print(sum(num_valid_2))