"""
--- Day 5: How About a Nice Game of Chess? ---

The eight-character password for the door is generated one character at a time
by finding the MD5 hash of some Door ID (your puzzle input) and an increasing
integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal
representation starts with five zeroes. If it does, the sixth character in the
hash is the next character of the password.
"""

import hashlib


def door_password(door_id, position_based) -> str:
    """ Determine the password from part one"""
    int_idx = 0

    if not position_based:
        password = ""
    else:
        password_arr = ["_", "_", "_", "_", "_", "_", "_", "_"]
        password = ""

    # Loop until eight characters have been found
    while "_" in password_arr:

        # Combine the door_id and index
        door_id_idx = door_id + str(int_idx)

        # Create the hash of the door index and door id
        idx_hash = hashlib.md5(door_id_idx.encode('utf-8')).hexdigest()

        # Check if the hash starts with five zeros
        if idx_hash.startswith("00000"):

            if not position_based:

                # Save the char after the 5 zeros
                password += idx_hash[5]
                print(idx_hash[5], end="")

            else:
                # Check the position is valid and in the password
                if idx_hash[5].isdigit() and (0 <= int(idx_hash[5])
                                              < len(password_arr)):

                    if password_arr[int(idx_hash[5])] == "_":

                        password_arr[int(idx_hash[5])] = idx_hash[6]
                        print("".join(password_arr))

        int_idx += 1

    return password


input_door_id = "ugkcyxxp"
sample_door_id = "abc"

# Part 1
#door_password(input_door_id, False)

door_password(input_door_id, True)
