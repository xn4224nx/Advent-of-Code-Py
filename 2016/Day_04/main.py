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

With all the decoy data out of the way, it's time to decrypt this list and get
moving.

The room names are encrypted by a state-of-the-art shift cipher, which is
nearly unbreakable without the right software. However, the information kiosk
designers at Easter Bunny HQ were not expecting to deal with a master
cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a
number of times equal to the room's sector ID. A becomes B, B becomes C, Z
becomes A, and so on. Dashes become spaces.

PART 2: What is the sector ID of the room where North Pole objects are stored?
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


def decrypt_room_name(room: dict) -> str:
    """
    Determine what the unencrypted name of the room is.
    """
    clear_name = ""

    for char in room["name"]:
        if char == "-":
            clear_name += " "
            continue

        clear_name += chr(ord("a") + (ord(char) - ord("a") + room["sec_id"]) % 26)

    return clear_name


def sum_real_room_sector_ids(all_rooms: list[dict]) -> int:
    """
    Return the sum of sector ids of all the real rooms.
    """
    sector_sum = 0

    for u_room in all_rooms:
        if is_room_real(u_room):
            sector_sum += u_room["sec_id"]

    return sector_sum


def find_northpole_room_id(all_rooms: list[dict]) -> int:
    """
    Determine the id of the room that has the name `northpole object storage`
    """
    for room in room_data:
        if decrypt_room_name(room) == "northpole object storage":
            return room["sec_id"]


if __name__ == "__main__":
    room_data = read_room_data("./data/input.txt")
    print(
        f"Part 1 = {sum_real_room_sector_ids(room_data)}\n"
        f"Part 2 = {find_northpole_room_id(room_data)}\n"
    )
