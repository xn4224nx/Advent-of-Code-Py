"""
KnotHash class taken from Day 10.
"""

from functools import reduce
from operator import xor


class KnotHash:
    def __init__(self, message: str):
        self.max_element = 255
        self.pos = 0
        self.skip_size = 0
        self.rope = [x for x in range(self.max_element + 1)]
        self.lengths = [ord(x) for x in message] + [
            17,
            31,
            73,
            47,
            23,
        ]

    def reverse(self, rev_len: int):
        """
        Reverse the specified elements in the rope.
        """
        # Select the values in the slice
        spl_slice = [self.rope[(self.pos + x) % len(self.rope)] for x in range(rev_len)]

        # Reverse the values
        spl_slice = spl_slice[::-1]

        # Reinsert the values
        for idx in range(rev_len):
            self.rope[(self.pos + idx) % len(self.rope)] = spl_slice[idx]

        # Increase the position and skip size
        self.pos = (self.pos + rev_len + self.skip_size) % len(self.rope)
        self.skip_size += 1

    def run_rounds(self, num_rounds: int = 64) -> int:
        """
        For the hashing algorithm run rounds of hashing.
        """
        for _ in range(num_rounds):
            for skip in self.lengths:
                self.reverse(skip)

    def final_result(self) -> int:
        """
        Calculate the result of finding the first two numbers in the rope.
        """
        self.run_rounds(1)
        return self.rope[0] * self.rope[1]

    def compress_hash(self) -> str:
        """
        Convert the sparse hash of decimal numbers into a dense hash of a string
        of hexidecimal numbers.
        """
        final_chars = []

        # Chunk the rope into blocks of 16
        for idx in range(0, len(self.rope), 16):
            block = (self.rope[x] for x in range(idx, idx + 16))

            # XOR all the elements
            xor_result = reduce(xor, block)

            # Convert to a hexidecimal number and pad with zeros
            final_chars.append(hex(xor_result)[2:].zfill(2))

        return "".join(final_chars)

    def calc_digest(self) -> str:
        """
        Determine the final hash  from the specified byte input.
        """
        self.run_rounds()
        return self.compress_hash()
