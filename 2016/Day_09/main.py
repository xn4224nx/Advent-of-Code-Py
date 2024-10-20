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
"""


def decompress_data(data_file: str) -> str:
    """
    Take one sweep across the data file string and decompress it once according
    to the markers.
    """
    decomp = ""

    with open(data_file) as fp:
        initial = fp.read()

    marker_active = False
    marker_reading = False
    marker_len = ""
    marker_rep = ""
    marker_dupli = ""

    # Read the string line by line
    for char in initial:

        if char.isspace():
            pass

        # Detect the start of a marker
        elif not marker_active and char == "(":
            marker_reading = True

        # Detect the end of a marker
        elif marker_reading and char == ")":
            marker_reading = False
            marker_active = True
            marker_rep = int(marker_rep)

        # Check for marker reading number changing
        elif marker_reading and char == "x":
            marker_len = int(marker_len)

        # Parse the first marker values
        elif marker_reading and type(marker_len) is str:
            marker_len += char

        # Parse the second marker values
        elif marker_reading and type(marker_len) is int:
            marker_rep += char

        # Read the current char if a marker repetition is active
        elif marker_active and marker_len > 0:
            marker_dupli += char
            marker_len -= 1

            # Catch the end of a marker
            if marker_len <= 0:
                marker_active = False
                decomp += marker_rep * marker_dupli
                marker_len = ""
                marker_rep = ""
                marker_dupli = ""

        # Read a normal character
        else:
            decomp += char

    return decomp

if __name__ == "__main__":
    print(f"Part 1 = {len(decompress_data('./data/input.txt'))}")
