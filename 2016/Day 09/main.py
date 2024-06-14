"""
--- Day 9: Explosives in Cyberspace ---

Whitespace is ignored. To indicate that some sequence should be repeated, a
marker is added to the file, like (10x2). To decompress this marker, take the
subsequent 10 characters and repeat them 2 times. Then, continue reading the
file after the repeated data. The marker itself is not included in the
decompressed output.

If parentheses or other characters appear within the data referenced by a
marker, that's okay - treat it like normal data, not a marker, and then resume
looking for markers after the decompressed section.
"""

import re


def decompress_str(comp_str: str) -> str:
    """Decompress one string."""

    # Key variables
    marker_re_pat0 = r"\(([0-9]+)x([0-9]+)\)"
    new_str = ""
    marker_pos: list[tuple[int, int]] = []
    marker_text: list[tuple[int, int]] = []

    cnt = 0

    # Iterate over all the markers in the string
    for match in re.finditer(marker_re_pat0, comp_str):

        # Find the position of every marker in the string
        marker_pos.append((match.start(0), match.end(0)))

        # Extract the marker characters and multiplication
        marker_text.append((int(match.group(1)), int(match.group(2))))

        curr_marker_coverage = marker_pos[cnt][1] + marker_text[cnt][0]

        # Check if this marker is in the previous markers range
        if cnt > 0:
            prev_marker_coverage = marker_pos[cnt-1][1] + marker_text[cnt-1][0]

            # If the current marker overlaps remove it
            if match.start(0) < prev_marker_coverage:
                marker_pos.pop()
                marker_text.pop()
                continue

        # Extract all the text before the marker
        if cnt == 0:
            new_str += comp_str[:marker_pos[cnt][0]]
        else:
            new_str += comp_str[prev_marker_coverage:marker_pos[cnt][0]]

        # For each marker replicate the compressed text and add it to the new
        # string.
        new_str += comp_str[marker_pos[cnt][1]:
                            marker_pos[cnt][1] +
                            marker_text[cnt][0]] * \
                   marker_text[cnt][1]

        cnt += 1

    # If there are no markers in the string return it
    if not marker_pos:
        return comp_str
    else:
        # Add text after the final marker to the string
        new_str += comp_str[curr_marker_coverage:]

    return new_str


def decompress_len(comp_str: str) -> str:
    """Determine the length of the decompressed string."""

    # Key variables about the markers
    marker_re_pat0 = r"\(([0-9]+)x([0-9]+)\)"
    marker_pos: list[tuple[int, int]] = []
    marker_text: list[tuple[int, int]] = []

    # Count of the marker and the new string
    cnt = 0
    str_len = 0

    # Iterate over all the markers in the string
    for match in re.finditer(marker_re_pat0, comp_str):

        # Find the position of every marker in the string
        marker_pos.append((match.start(0), match.end(0)))

        # Extract the marker characters and multiplication
        marker_text.append((int(match.group(1)), int(match.group(2))))

        curr_marker_coverage = marker_pos[cnt][1] + marker_text[cnt][0]

        # Check if this marker is in the previous markers range

        # If the current marker overlaps remove it or add it to the marker list



# Load the string from file
input_str = open("data/input.txt").read()

# Remove all whitespace
input_str = re.sub(r'\s+', '', input_str)
input_str = "X(8x2)(3x3)ABCY"

output_str = decompress_str(input_str)

print(input_str)
print(output_str)
print(len(output_str))
