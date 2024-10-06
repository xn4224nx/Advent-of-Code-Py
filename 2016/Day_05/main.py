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


def hash_door_index(door: str, index: int) -> str:
    """
    Find the hash of the string and a particular index
    """
    pass


def find_password(door_id: str) -> str:
    """
    Search the for the 8 character password for a room with a particular
    door id.
    """
    pass


if __name__ == "__main__":
    pass
