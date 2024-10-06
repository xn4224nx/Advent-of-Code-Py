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

As the door slides open, you are presented with a second door that uses a
slightly more inspired security mechanism. Clearly unimpressed by the last
version (in what movie is the password decrypted in order?!), the Easter Bunny
engineers have worked out a better solution.

Instead of simply filling in the password from left to right, the hash now also
indicates the position within the password to fill. You still look for hashes
that begin with five zeroes; however, now, the sixth character represents the
position (0-7), and the seventh character is the character to put in that
position.

A hash result of 000001f means that f is the second character in the password.
Use only the first result for each position, and ignore invalid positions.

PART 2: Given the actual Door ID and this new method, what is the password? Be
        extra proud of your solution if it uses a cinematic "decrypting"
        animation.
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


def find_positional_password(door_id: str) -> str:
    """
    Search for the eight character password using hashes that start with
    five zeroes. The fifth char determines the position of the inserted
    character and the sixth character is inserted.
    """
    password = ["*" for _ in range(8)]
    idx = 0

    while "*" in password:
        digest = hash_door_index(door_id, idx)

        # Has a new character in the password been found?
        if digest[:5] == "00000" and digest[5].isdigit():
            pas_idx = int(digest[5])

            # Check that the pass index is valid and hasn't already been found
            if pas_idx < 8 and password[int(digest[5])] == "*":
                password[int(digest[5])] = digest[6]
                print("", end=f"\r{''.join(password)}")

        idx += 1

    return "".join(password)


if __name__ == "__main__":
    door_code_1 = find_password("ffykfhsq")
    print(f"\nPart 1 = '{door_code_1}'\n")

    door_code_2 = find_positional_password("ffykfhsq")
    print(f"\nPart 2 = '{door_code_2}'\n")
