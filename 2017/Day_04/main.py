"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a
passphrase instead of simply a password. A passphrase consists of a series of
words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    -   aa bb cc dd ee is valid.
    -   aa bb cc dd aa is not valid - the word aa appears more than once.
    -   aa bb cc dd aaa is valid    - aa and aaa count as different words.

PART 1: The system's full passphrase list is available as your puzzle input. How
        many passphrases are valid?

For added security, yet another system policy has been put in place. Now, a
valid passphrase must contain no two words that are anagrams of each other -
that is, a passphrase is invalid if any word's letters can be rearranged to form
any other word in the passphrase.

For example:

    -   abcde fghij is a valid passphrase.

    -   abcde xyz ecdab is not valid - the letters from the third word can be
        rearranged to form the first word.

    -   a ab abc abd abf abj is a valid passphrase, because all letters need to
        be used when forming another word.

    -   iiii oiii ooii oooi oooo is valid.

    -   oiii ioii iioi iiio is not valid - any of these words can be rearranged
        to form any other word.

PART 2: Under this new system policy, how many passphrases are valid?
"""


class SecuritySystem:
    def __init__(self, passphrase_file: str):
        self.all_passphrases = []

        with open(passphrase_file, "r") as fp:
            for line in fp.readlines():
                self.all_passphrases.append(line.strip())

    def valid_phrase(self, passphrase: str, anagram: bool = False) -> bool:
        """
        Extract the words in a passphrase and determine if there are any
        duplicates, if so the passphrase is not valid.
        """
        words = passphrase.split()

        # If anagrams are excluded sort the letters in the word so they will be
        # marked as duplicates when added to a set
        if anagram:
            words = ["".join(sorted(x)) for x in words]

        # Check for any duplicate words in the passphrase by comparing the set
        num_words = len(words)
        unique_words = len(set(words))

        return num_words == unique_words

    def count_valid_passphrases(self, anagram: bool = False) -> int:
        """
        Count the number of passphrases that contain no duplicate words.
        """
        return sum([self.valid_phrase(x, anagram) for x in self.all_passphrases])


if __name__ == "__main__":
    sec_sys = SecuritySystem("./data/input.txt")
    print(f"Part 1 = {sec_sys.count_valid_passphrases()}")
    print(f"Part 1 = {sec_sys.count_valid_passphrases(True)}")
