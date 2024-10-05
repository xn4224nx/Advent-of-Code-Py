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


def read_room_data(data_file: str) -> list[dict]:
    """
    Read the room data and return a list of structured data.
    """
    pass


def is_room_real(room: dict) -> bool:
    """
    Determine if a room is real. It is real  if the checksum is the five most
    common letters in the encrypted name, in order, with ties broken by
    alphabetization.
    """
    pass


def sum_real_room_sector_ids(all_rooms: list[dict]) -> int:
    """
    Return the sum of sector ids of all the real rooms.
    """
    pass


if __name__ == "__main__":
    pass
