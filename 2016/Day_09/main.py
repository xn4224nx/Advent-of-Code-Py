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


def read_data(data_file: str) -> str:
    """
    Read the compressed data file and remove the trailing whitespace.
    """
    with open(data_file) as fp:
        return fp.read().strip()


def find_markers(compressed_data: str, recursive: bool) -> dict:
    """
    Determine the marker groups and their statistics. If the the groups are not
    recursive remove the ones that are treated as data.
    """
    marker_pat = re.compile(r"\(([0-9]+)x([0-9]+)\)")

    # Find the location, magnitude and range of all markers
    markers = [
        {
            "len": int(x.group(1)),
            "rep": int(x.group(2)),
            "start": x.start(),
            "end": x.end(),
            "copies": 1,
        }
        for x in marker_pat.finditer(compressed_data)
    ]

    # Remove markers that are treated as data
    rm_mkr_idx = []
    markers_to_rm = []
    for mkr_idx in range(len(markers)):

        # If a marker will be removed it can't remove other markers.
        if not recursive and mkr_idx in rm_mkr_idx:
            continue

        # Check every other marker to see if it get copied by the current one or
        # ignored because it gets treated as data.
        for nxt_mkr_idx in range(mkr_idx + 1, len(markers)):

            end_of_mkr = markers[mkr_idx]["len"] + markers[mkr_idx]["end"]

            # Ensure the next marker is in range
            if end_of_mkr < markers[nxt_mkr_idx]["start"]:
                break

            # Increase the next marker by the current copies size
            if recursive:
                markers[nxt_mkr_idx]["copies"] *= markers[mkr_idx]["rep"]

            # Or set this marker to be treated as data ie remove its record
            else:
                markers_to_rm.append(nxt_mkr_idx)

    # Remove the markers that are treated as data
    for mkr_idx in markers_to_rm:
        if mkr_idx < len(markers):
            del markers[mkr_idx]

    return markers


def calc_len(file_path: str, recursive: bool) -> int:
    """
    Calculate the decompressed length of a raw string, optionally implementing
    recursive decompression.
    """
    uncompr = read_data(file_path)
    marks = find_markers(uncompr, recursive)

    # Deal with there being no markers
    if not marks:
        return len(uncompr)

    # Record the characters at the start of the string that never get duplicated
    total_len = marks[0]["start"]

    # Calculate the contribution each marker makes
    for mkr_idx in range(len(marks)):

        # At what index does the next marker or the end of string occur
        if mkr_idx < len(marks) - 1:
            nxt_mkr_idx = marks[mkr_idx + 1]["start"]
        else:
            nxt_mkr_idx = len(uncompr)

        # Determine what length of chars get multiplied by the current marker
        char_diff = min(nxt_mkr_idx - marks[mkr_idx]["end"], marks[mkr_idx]["len"])

        # Add in the characters that get multiplied
        total_len += char_diff * marks[mkr_idx]["rep"] * marks[mkr_idx]["copies"]

        # Add in characters that are at the end but don't get multiplied
        total_len += max(0, nxt_mkr_idx - char_diff - marks[mkr_idx]["end"])

    return total_len


if __name__ == "__main__":
    pass
