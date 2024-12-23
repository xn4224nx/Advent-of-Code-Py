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


def reverse_number(data: str) -> str:
    """
    Reverse a string representation of a binary number.
    """
    return data[::-1]


def invert_number(data: str) -> str:
    """
    In the supplied number swap every zero for a one and vice versa.
    """
    new_data = []

    for char in data:
        if char == "0":
            new_data.append("1")
        else:
            new_data.append("0")

    return "".join(new_data)


def dragon_fold(data: str) -> str:
    """
    Transform the initial data one step using the dragon curve technique.
    """
    return data + "0" + invert_number(reverse_number(data))


def checksum(data: str) -> str:
    """
    Calculate the checksum for a piece of binary data.
    """
    ch_sum = [x for x in data]

    # Keep halving the checksum until its length is odd
    while True:
        new_ch_sum = []

        # evaluate the pairs of the checksum
        for idx in range(1, len(ch_sum), 2):
            if ch_sum[idx] == ch_sum[idx - 1]:
                new_ch_sum.append("1")
            else:
                new_ch_sum.append("0")

        # Overwrite the old checksum
        ch_sum = new_ch_sum

        if len(ch_sum) % 2 != 0:
            break

    return "".join(ch_sum)


def disk_fill_checksum(seed_data: str, fill_size: int) -> str:
    """
    Determine what the checksum will be for the data that would fill the
    specified size.
    """
    data = seed_data[:]

    # Expand the data until it is at or above the fill size
    while len(data) < fill_size:
        data = dragon_fold(data)

    # Only include the exact number of bits we need
    data = data[:fill_size]

    # Calculate the checksum of this data
    return checksum(data)


if __name__ == "__main__":
    print(f"Part 1 = {disk_fill_checksum('10111011111001111', 272)}")
    print(f"Part 2 = {disk_fill_checksum('10111011111001111', 35651584)}")
