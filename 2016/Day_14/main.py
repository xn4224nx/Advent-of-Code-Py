"""
--- Day 14: One-Time Pad ---

In order to communicate securely with Santa while you're on this mission, you've
been using a one-time pad that you generate using a pre-agreed algorithm.
Unfortunately, you've run out of keys in your one-time pad, and so you need to
generate some more.

To generate keys, you first get a stream of random data by taking the MD5 of a
pre-arranged salt (your puzzle input) and an increasing integer index (starting
with 0, and represented in decimal); the resulting MD5 hash should be
represented as a string of lowercase hexadecimal digits.

However, not all of these MD5 hashes are keys, and you need 64 new keys for
your one-time pad. A hash is a key only if:

    -   It contains three of the same character in a row, like 777. Only
        consider the first such triplet in a hash.

    -   One of the next 1000 hashes in the stream contains that same character
        five times in a row, like 77777.

Considering future hashes for five-of-a-kind sequences does not cause those
hashes to be skipped; instead, regardless of whether the current hash is a key,
always resume testing for keys starting with the very next hash.

PART 1: Given the actual salt in your puzzle input, what index produces your
        64th one-time pad key?
"""


class KeyGenerator:
    def __init__(self, salt: str):
        pass

    def salted_hash(self) -> str:
        """
        Create a MD5 hash according to the current index and the pre-definined
        salt.
        """
        pass

    def scan_for_keys(self, num_required: int) -> int:
        """
        Search for keys that match the criteria and return the index of the last
        key found.
        """
        pass


if __name__ == "__main__":
    pass
