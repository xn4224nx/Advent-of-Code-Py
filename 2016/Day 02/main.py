"""
--- Day 2: Bathroom Security ---

The document goes on to explain that each button to be pressed can be found by
starting on the previous button and moving to adjacent buttons on the keypad:
U moves up, D moves down, L moves left, and R moves right. Each line of
instructions corresponds to one button, starting at the previous button (or,
for the first line, the "5" button); press whatever button you're on at the
end of each line. If a move doesn't lead to a button, ignore it.

"""

import numpy as np


def final_position(start_pos, instruct_str) -> list:
    """
    Determine the final position on the key pad after a line of instructions.
    """

    curr_pos = start_pos.copy()

    # For a line of instructions determine the final number
    for direct in instruct_str:

        # Move the position according to the direction
        if direct == 'U':
            curr_pos[0] -= 1
        elif direct == 'D':
            curr_pos[0] += 1
        elif direct == 'L':
            curr_pos[1] -= 1
        elif direct == 'R':
            curr_pos[1] += 1

        # Correct positions that have gone outside the number pad
        if curr_pos[0] < 0:
            curr_pos[0] = 0

        if curr_pos[1] < 0:
            curr_pos[1] = 0

        if curr_pos[0] >= num_pad.shape[0]:
            curr_pos[0] = num_pad.shape[0] - 1

        if curr_pos[1] >= num_pad.shape[1]:
            curr_pos[1] = num_pad.shape[1] - 1

    return curr_pos


def final_position2(start_pos, instruct_str, num_pad_arr) -> list:
    """Work out the final position on an inhomogeneous array."""

    curr_pos = start_pos.copy()

    # For a line of instructions determine the final number
    for direct in instruct_str:

        old_pos = curr_pos.copy()

        # Move the position according to the direction
        if direct == 'U':
            curr_pos[0] -= 1
        elif direct == 'D':
            curr_pos[0] += 1
        elif direct == 'L':
            curr_pos[1] -= 1
        elif direct == 'R':
            curr_pos[1] += 1

        if curr_pos[0] < 0:
            curr_pos[0] = 0

        if curr_pos[1] < 0:
            curr_pos[1] = 0

        if curr_pos[0] > 4:
            curr_pos[0] = 4

        if curr_pos[1] > 4:
            curr_pos[1] = 4

        try:
            if num_pad_arr[curr_pos[0]][curr_pos[1]] is None:
                curr_pos = old_pos.copy()

        except:
            curr_pos = old_pos.copy()

        print(num_pad_arr[curr_pos[0]][curr_pos[1]])

    print()

    return curr_pos


# Define the entry keypad
num_pad = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
num_pad2 = [[None, None, 1, None, None],
            [None, 2, 3, 4, None],
            [5, 6, 7, 8, 9],
            [None, 'A', 'B', 'C', None],
            [None, None, 'D', None, None]]

# Where do you start in the key pad?
coord = [1, 1]
coord2 = [2, 0]

# Load instructions from file
data = open("data/input.txt").read().splitlines()

code = ""
code2 = ""

print(num_pad2[coord2[0]][coord2[1]])

for line in data:

    # Find where the instructions lead
    # coord = final_position(coord, line)
    # code += str(num_pad[coord[0], coord[1]])

    coord2 = final_position2(coord2, line, num_pad2)
    code2 += str(num_pad2[coord2[0]][coord2[1]])

print(code)
print(code2)
