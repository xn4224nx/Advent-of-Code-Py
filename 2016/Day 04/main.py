"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course,
the list is encrypted and full of decoy data, but the instructions to decode
the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes)
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in
the encrypted name, in order, with ties broken by alphabetization.

What is the sum of the sector IDs of the real rooms?

"""

import re
from collections import Counter


def create_checksum(room_name) -> str:
    """Create what the room name checksum should be."""

    check_sum = ""

    # Remove the dashes
    room_name = room_name.replace('-', '')

    # Sort the letters alphabetically
    room_name = ''.join(sorted(room_name))

    for char in Counter(room_name).most_common():
        check_sum += char[0]

    return check_sum[:5]


def decrypt_room_name(room_name, sec_id) -> str:
    """
    To decrypt a room name, rotate each letter forward through the alphabet a
    number of times equal to the room's sector ID.

    Dashes become spaces.
    """

    new_name = ""

    for char in room_name:

        # Dashes become spaces
        if char == '-':
            new_name += " "
        else:
            new_name += chr(ord('a') + ((ord(char) - ord('a') + sec_id) % 26))

    return new_name


# Load the encrypted data
encrypt_ls = open("data/input.txt").read().splitlines()

# Parse the room information
encrypt_ls = [re.findall(r"([a-z\-]+)\-([0-9]+)\[([a-z]+)\]", x)[0]
              for x in encrypt_ls]

room_sum = 0
room_names = {}


# For each room calculate the checksum
for room in encrypt_ls:

    if create_checksum(room[0]) == room[2]:
        room_sum += int(room[1])
        room_names[decrypt_room_name(room[0], int(room[1]))] = int(room[1])

# Part 2
for name in room_names:
    if "north" in name:
        print(name, room_names[name])

# Part 1
print(room_sum)






