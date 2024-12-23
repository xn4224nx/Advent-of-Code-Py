"""
--- Day 16: Dragon Checksum ---

You're done scanning this part of the network, but you've left traces of your
presence. You need to overwrite some disks with random-looking data to cover
your tracks and update the local security system with a new checksum for those
disks.

For the data to not be suspicious, it needs to have certain properties; purely
random data will be detected as tampering. To generate appropriate random data,
you'll need to use a modified dragon curve.

Start with an appropriate initial state (your puzzle input). Then, so long as
you don't have enough data yet to fill the disk, repeat the following steps:

    -   Call the data you have at this point "a".
    -   Make a copy of "a"; call this copy "b".
    -   Reverse the order of the characters in "b".
    -   In "b", replace all instances of 0 with 1 and all 1s with 0.
    -   The resulting data is "a", then a single 0, then "b".

Repeat these steps until you have enough data to fill the desired disk.

Once the data has been generated, you also need to create a checksum of that
data. Calculate the checksum only for the data that fits on the disk, even if
you generated more data than that in the previous step.

The checksum for some given data is created by considering each non-overlapping
pair of characters in the input data. If the two characters match (00 or 11),
the next checksum character is a 1. If the characters do not match (01 or 10),
the next checksum character is a 0. This should produce a new string which is
exactly half as long as the original. If the length of the checksum is even,
repeat the process until you end up with a checksum with an odd length.

PART 1: The first disk you have to fill has length 272. Using the initial state
        in your puzzle input, what is the correct checksum?
"""


def convert_2_bin(number: str) -> int:
    """
    Get the true number from a string of ones and zeros that represent a binary
    number.
    """
    pass


def convert_2_str(number: int) -> str:
    """
    Convert a raw binary number to its string representation comprised of ones
    and zeros.
    """
    pass


def dragon_fold(data: int) -> int:
    """
    Transform the initial data one step using the dragon curve technique.
    """
    pass


def checksum(data: int) -> int:
    """
    Calculate the checksum for a piece of binary data.
    """
    pass


def disk_fill_checksum(seed_data: str, fill_size: int) -> str:
    """
    Determine what the checksum will be for the data that would fill the
    specified size.
    """
    pass


if __name__ == "__main__":
    pass
