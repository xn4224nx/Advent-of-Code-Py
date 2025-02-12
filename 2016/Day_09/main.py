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
        self.markers = []
        self.orig_str_len = 0

        # Keep account of the internal workings of the current marker
        in_marker = False
        mkr_start_idx = 0
        partial_num = ""
        temp_num = 0

        # Open the file and iterate over the chars one by one
        with open(datafile, "r") as fp:
            for line in fp:
                for idx, char in enumerate(line):

                    # Ignore whitespace
                    if char.isspace():
                        continue

                    # Count the lenght of the original input
                    self.orig_str_len += 1

                    # Detect the start of a marker
                    if char == "(":
                        mkr_start_idx = idx
                        in_marker = True

                    # Detect the end of a marker
                    elif char == ")":
                        in_marker = False

                        # Save the current marker
                        self.markers.append(
                            (
                                mkr_start_idx,
                                idx,
                                temp_num,
                                int(partial_num),
                            )
                        )

                        mkr_start_idx = 0
                        partial_num = ""
                        temp_num = 0

                    # Detect a change in numbers
                    elif char == "x" and in_marker:
                        temp_num = int(partial_num)
                        partial_num = ""

                    # Detect digits inside the marker
                    elif in_marker and char.isdigit():
                        partial_num += char

    def decomp_len(self, recursive: bool) -> int:
        """
        Calculate the length of the data when it is decompressed, either
        recursively or ignoring markers within other markers.
        """

        # If there are no markers just return the original length
        if not self.markers:
            return self.orig_str_len

        # When the decompression is not recusive some markers are ignored.
        if not recursive:
            ignored_markers = []
            valid_markers = []

            # The first marker is always valid but others are invalid if
            # a previous marker overlaps with them.
            for mk_idx in range(len(self.markers)):
                if mk_idx not in ignored_markers:
                    valid_markers.append(list(self.markers[mk_idx]))

                    # Now check all the coming markers to see if they overlap
                    # with the current one and thus become invalid
                    curr_mkr_idx_reach = (
                        self.markers[mk_idx][1] + self.markers[mk_idx][2]
                    )

                    for n_mk_idx in range(mk_idx + 1, len(self.markers)):
                        if curr_mkr_idx_reach > self.markers[n_mk_idx][0]:
                            ignored_markers.append(n_mk_idx)
                        else:
                            break
        else:
            valid_markers = [list(x) for x in self.markers]

        # Iterate over the markers and calculate the distance between them
        sparse_data = []
        for mk_idx in range(len(valid_markers)):
            start_idx = valid_markers[mk_idx][1] + 1

            # Determine where this markers effect ends
            if mk_idx == len(valid_markers) - 1:
                end_idx = self.orig_str_len - 1
            else:
                end_idx = valid_markers[mk_idx + 1][0] - 1

            # Transform the data into a sparse array
            for dt_idx in range(start_idx, end_idx + 1):
                sparse_data.append([dt_idx, 1])

        # Iterate over the markers and determine how many times the data
        # gets multiplied.
        for mk_idx in range(len(valid_markers)):
            mk_reach = valid_markers[mk_idx][1] + valid_markers[mk_idx][2]

            # Determine the data the marker covers
            for dt_idx in range(len(sparse_data)):
                data_loc = sparse_data[dt_idx][0]

                if data_loc <= mk_reach and data_loc > valid_markers[mk_idx][0]:
                    sparse_data[dt_idx][1] *= valid_markers[mk_idx][3]

        # Sum all the elements of sparse data
        return valid_markers[0][0] + sum([x[1] for x in sparse_data])


if __name__ == "__main__":
    sec_data = CompressedData("./data/input.txt")
    print(f"Part 1 = {sec_data.decomp_len(False)}")
    print(f"Part 2 = {sec_data.decomp_len(True)}")
