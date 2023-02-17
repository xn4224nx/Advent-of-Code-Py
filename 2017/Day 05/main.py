"""
--- Day 5: A Maze of Twisty Trampolines, All Alike ---

The message includes a list of the offsets for each jump. Jumps are relative:
-1 moves to the previous instruction, and 2 skips the next one. Start at the
first instruction in the list. The goal is to follow the jumps until one leads
outside the list.


# Part 1

In addition, these instructions are a little strange; after each jump, the
offset of that instruction increases by 1. So, if you come across an offset
of 3, you would move three instructions forward, but change it to a 4 for
the next time it is encountered.


# Part 2

Now, the jumps are even stranger: after each jump, if the offset was three or
more, instead decrease it by 1. Otherwise, increase it by 1 as before.

"""


def load_jump_instructions(fp: str) -> list[int]:
    """Load the jump instructions from file."""

    data = open(fp, "r").read().splitlines()
    data = [int(x) for x in data]

    return data


def run_jumps(instructs: list[int], strange: bool) -> int:
    """
    Run through the list of instructions and return how many steps it
    takes to finish.
    """

    data = instructs.copy()
    index = 0
    steps = 0

    while True:

        # What is the jump the instructions say should happen
        jump = data[index]

        # Increment the current instruction
        if strange and jump >= 3:
            data[index] -= 1
        else:
            data[index] += 1

        # Where does the new jump go
        index += jump

        # Exit the loop if the index is not pointing to a valid instruction
        steps += 1
        if index < 0 or index >= len(data):
            break

    return steps


jumps = load_jump_instructions("data/input.txt")

# Part 1
print(run_jumps(jumps, False))

# Part 2
print(run_jumps(jumps, True))
