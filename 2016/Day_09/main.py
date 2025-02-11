"""
--- Day 9: Explosives in Cyberspace ---

Wandering around a secure area, you come across a datalink port to a new part of
the network. After briefly scanning it for interesting files, you find one file
in particular that catches your attention. It's compressed with an experimental
format, but fortunately, the documentation for the format is nearby.

The format compresses a sequence of characters. Whitespace is ignored. To
indicate that some sequence should be repeated, a marker is added to the file,
like (10x2). To decompress this marker, take the subsequent 10 characters and
repeat them 2 times. Then, continue reading the file after the repeated data.
The marker itself is not included in the decompressed output.

If parentheses or other characters appear within the data referenced by a
marker, that's okay - treat it like normal data, not a marker, and then resume
looking for markers after the decompressed section.

PART 1: What is the decompressed length of the file (your puzzle input)? Don't
        count whitespace.

Apparently, the file actually uses version two of the format.

In version two, the only difference is that markers within decompressed data are
decompressed. This, the documentation explains, provides much more substantial
compression capabilities, allowing many-gigabyte files to be stored in only a
few kilobytes.

PART 2: What is the decompressed length of the file using this improved format?
"""

import re


class CompressedData:
    def __init__(self, datafile: str):
        pass

    def decomp_len(self, recursive: bool) -> int:
        """
        Calculate the length of the data when it is decompressed, either
        recursively or ignoring markers within other markers.
        """
        pass


if __name__ == "__main__":
    sec_data = CompressedData("./data/input.txt")
    print(f"Part 1 = {sec_data.decomp_len(False)}")
    print(f"Part 2 = {sec_data.decomp_len(True)}")
