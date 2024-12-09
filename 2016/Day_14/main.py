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

import hashlib
from collections import deque


class KeyGenerator:
    def __init__(self, salt: str):
        self.salt = salt
        self.index = 0
        self.key_idxs = []

    def salted_hash(self) -> str:
        """
        Create a MD5 hash according to the current index and the pre-definined
        salt.
        """
        raw_msg = self.salt + str(self.index)
        return hashlib.md5(raw_msg.encode()).hexdigest()

    def extract_trips_quints(self, digest: str) -> dict[str:[str]]:
        """
        Find the first triple in a message digest and return the character that
        get repeated. Also find the quintets in the digest and return those.
        Everything is packages in a dictionary of labeled parts
        """
        trips = []
        quints = []

        for idx in range(len(digest)):

            # Catch a triplet
            if (
                idx >= 2
                and not trips
                and all(x == digest[idx - 2] for x in digest[idx - 2 : idx + 1])
            ):
                trips.append(digest[idx])

            # Catch a quintlet
            if idx >= 4 and all(x == digest[idx] for x in digest[idx - 4 : idx + 1]):
                quints.append(digest[idx])

        return {"trips": trips, "quints": quints}

    def scan_for_keys(self, num_required: int) -> int:
        """
        Search for keys that match the criteria and return the index of the last
        key found.
        """
        pot_keys = deque()
        while len(self.key_idxs) < num_required:

            # Remove potential keys that have expired
            for idx_pkey in range(len(pot_keys)):

                if pot_keys[idx_pkey]["index"] < self.index - 1000:
                    pot_keys.popleft()
                else:
                    break

            # Generate the digest for this index
            digest = self.salted_hash()

            # Look for triplets and quintets
            idents = self.extract_trips_quints(digest)

            # Check for a comformation of an existing key
            for pkey in pot_keys:
                for quint in idents["quints"]:

                    # Check for a validated key
                    if quint == pkey["char"]:
                        self.key_idxs.append(pkey["index"])

            # Check for a new key and record its details
            if idents["trips"]:
                pot_keys.append({"index": self.index, "char": idents["trips"][0][0]})

            self.index += 1

        return self.key_idxs[-1]


if __name__ == "__main__":
    pass
