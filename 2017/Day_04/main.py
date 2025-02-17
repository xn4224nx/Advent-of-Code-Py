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
"""


class SecuritySystem:
    def __init__(self, passphrase_file: str):
        self.all_passphrases = []

        with open(passphrase_file, "r") as fp:
            for line in fp.readlines():
                self.all_passphrases.append(line.strip())

    def valid_phrase_dupe(self, passphrase: str) -> bool:
        """
        Extract the words in a passphrase and determine if there are any
        duplicates, if so the passphrase is not valid.
        """
        words = passphrase.split()
        num_words = len(words)
        unique_words = len(set(words))

        return num_words == unique_words

    def count_valid_passphrases(self) -> int:
        """
        Count the number of passphrases that contain no duplicate words.
        """
        return sum([self.valid_phrase_dupe(x) for x in self.all_passphrases])


if __name__ == "__main__":
    sec_sys = SecuritySystem("./data/input.txt")
    print(f"Part 1 = {sec_sys.count_valid_passphrases()}")
