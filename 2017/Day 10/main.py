"""
--- Day 10: Knot Hash ---

This hash function simulates tying a knot in a circle of string with 256 marks
on it. Based on the input to be hashed, the function repeatedly selects a span
of string, brings the ends together, and gives the span a half-twist to reverse
the order of the marks within it. After doing this many times, the order of the
marks is used to build the resulting hash.

To achieve this, begin with a list of numbers from 0 to 255, a current position
which begins at 0 (the first element in the list), a skip size (which starts
at 0), and a sequence of lengths (your puzzle input). Then, for each length:

    Reverse the order of that length of elements in the list, starting with the
    element at the current position.

    Move the current position forward by that length plus the skip size.

    Increase the skip size by one.

The list is circular; if the current position and the length try to reverse
elements beyond the end of the list, the operation reverses using as many extra
elements as it needs from the front of the list. If the current position moves
past the end of the list, it wraps around to the front. Lengths larger than the
size of the list are invalid.
"""

from functools import reduce


class KnotHash:

    def __init__(self, unknotted_length: int):

        self.skip_size = 0
        self.curr_idx = 0
        self.string = [x for x in range(unknotted_length)]
        self.sparse_ascii_rep = None
        self.dense_ascii_rep = None

    def increase_idx(self, increase):
        self.curr_idx += increase
        self.curr_idx %= len(self.string)

    def pinch_twist(self, pinch_len: int):
        """
        Reverse a section of the string starting from curr_idx to before
        curr_idx + pinch_len.
        """

        start = self.curr_idx
        end = (self.curr_idx + pinch_len) % len(self.string)

        # Detect the index going beyond the length of the string
        if self.curr_idx + pinch_len >= len(self.string):

            # Extract the parts of the string that will be flipped
            flip_part = self.string[start:] + self.string[:end]

            # Flip them
            flip_part = flip_part[::-1]

            # Insert them back into the string
            self.string[start:] = flip_part[:-len(self.string[:end])]
            self.string[:end] = flip_part[len(self.string[start:]):]

        else:
            self.string[start:end] = self.string[start:end][::-1]

        self.increase_idx(pinch_len + self.skip_size)

        # With each twist the skip length increases
        self.skip_size += 1

    def knots(self, pinch_lens: list[int]):

        for length in pinch_lens:
            self.pinch_twist(length)

    def convert_str_to_ascii(self, input_lens: str) -> list[int]:
        """
        Take a str and convert the characters to the ascii
        numbers they represent.

        It also adds [17, 31, 73, 47, 23] to the end of the converted list.
        """

        ascii_rep = [ord(x) for x in input_lens]
        ascii_rep += [17, 31, 73, 47, 23]

        self.sparse_ascii_rep = ascii_rep

    def dec_int_2_hex_str(self, numbers: list[int]) -> str:
        """Convert integers to its corresponding hex number in a string."""
        hex_rep = ""

        for num in numbers:
            hex_rep += f'{num:02x}'

        return hex_rep

    def create_dense_ascii(self):
        """Create a dense ascii out of the string."""

        dense_ascii = []

        for idx in range(16):
            dense_ascii.append(reduce(lambda x, y: x ^ y,
                                      self.string[idx*16:(idx+1)*16]))
        self.dense_ascii_rep = dense_ascii


# Part 1
ini_string = KnotHash(256)
ini_string.knots([63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24])
# print(ini_string.string[0]*ini_string.string[1])

# Part 2
hashed_string = KnotHash(256)
hashed_string.convert_str_to_ascii("")

print(hashed_string.sparse_ascii_rep)

for i in range(64):
    hashed_string.knots(hashed_string.sparse_ascii_rep)

hashed_string.create_dense_ascii()

print(hashed_string.string)
print(hashed_string.dec_int_2_hex_str(hashed_string.dense_ascii_rep))