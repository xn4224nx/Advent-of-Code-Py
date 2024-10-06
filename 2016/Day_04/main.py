"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course,
the list is encrypted and full of decoy data, but the instructions to decode the
list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes)
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in
the encrypted name, in order, with ties broken by alphabetization.

PART 1: What is the sum of the sector IDs of the real rooms?
"""

import re


def read_room_data(data_file: str) -> list[dict]:
    """
    Read the room data and return a list of structured data.
    """
    room_pat = re.compile(r"([0-9a-z\-]+)\-([0-9]+)\[([a-z]+)\]")
    rooms = []

    with open(data_file) as fp:
        for line in fp.readlines():
            room_parts = room_pat.search(line)
            rooms.append(
                {
                    "name": room_parts.group(1),
                    "sec_id": int(room_parts.group(2)),
                    "check_sum": room_parts.group(3),
                }
            )

    return rooms


def room_checksum(room_name: str) -> str:
    """
    Determine the checksum of a room.
    """
    char_cnts = {}

    # Count the incidents of characters in the room name
    for char in room_name:
        if char == "-":
            continue

        if char not in char_cnts:
            char_cnts[char] = 1
        else:
            char_cnts[char] += 1

    # Sort the dict by alphabetical order
    char_cnts = dict(sorted(char_cnts.items()))

    # Sort the characters in the name by occurance
    char_incidence = sorted(char_cnts, key=char_cnts.get, reverse=True)
    check_sum = "".join(char_incidence[:5])

    return check_sum


def is_room_real(room: dict) -> bool:
    """
    Determine if a room is real. It is real  if the checksum is the five most
    common letters in the encrypted name, in order, with ties broken by
    alphabetization.
    """
    return room_checksum(room["name"]) == room["check_sum"]


def sum_real_room_sector_ids(all_rooms: list[dict]) -> int:
    """
    Return the sum of sector ids of all the real rooms.
    """
    sector_sum = 0

    for u_room in all_rooms:
        if is_room_real(u_room):
            sector_sum += u_room["sec_id"]

    return sector_sum


if __name__ == "__main__":
    room_data = read_room_data("./data/input.txt")
    print(f"Part 1 = {sum_real_room_sector_ids(room_data)}")
