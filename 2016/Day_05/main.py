"""
--- Day 5: How About a Nice Game of Chess? ---

You are faced with a security door designed by Easter Bunny engineers that seem
to have acquired most of their security knowledge by watching hacking movies.

The eight-character password for the door is generated one character at a time
by finding the MD5 hash of some Door ID (your puzzle input) and an increasing
integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal
representation starts with five zeroes. If it does, the sixth character in the
hash is the next character of the password.

PART 1: Given the actual Door ID, what is the password?
"""

import hashlib


def hash_door_index(door: str, index: int) -> str:
    """
    Find the hash of the string and a particular index
    """
    return hashlib.md5(f"{door}{index}".encode("utf-8")).hexdigest()


def find_password(door_id: str) -> str:
    """
    Search the for the 8 character password for a room with a particular
    door id.
    """
    password = ""
    idx = 0

    # Find the digest for each door id and index
    while len(password) < 8:
        digest = hash_door_index(door_id, idx)

        # Has a new character in the password been found ?
        if digest[:5] == "00000":
            password += digest[5]
            print("", end=f"\r{password}")

        # Prepare to test the next index
        idx += 1

    return password


if __name__ == "__main__":
    door_code = find_password("ffykfhsq")
    print(f"\nPart 1 = '{door_code}'")
