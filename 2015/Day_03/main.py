"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid
of houses.

He begins by delivering a present to the house at his starting
location, and then an elf at the North Pole calls him via radio
and tells him where to move next. Moves are always exactly one
house to the north (^), south (v), east (>), or west (<). After
each move, he delivers another present to the house at his new
location.

However, the elf back at the north pole has had a little too
much eggnog, and so his directions are a little off, and Santa
ends up visiting some houses more than once.

PART 1: How many houses receive at least one present?

The next year, to speed up the process, Santa creates a robot
version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two
presents to the same starting house), then take turns moving
based on instructions from the elf, who is eggnoggedly reading
from the same script as the previous year.

PART 2: This year, how many houses receive at least one present?
"""


def read_directions(file_path: str) -> str:
    """
    Open the direction file and return a string of the file
    contents.
    """

    with open(file_path) as fp:
        contents = fp.read().rstrip()

    return contents


def houses_covered(directions: str, robo_santa=False) -> int:
    """
    What are the houses covered when Santa has a robot helper that
    uses every other instruction and Santa uses the other.
    """

    start_loc = (0, 0)
    visted_houses = {start_loc}

    r_loc = start_loc
    s_loc = start_loc

    for idx, char in enumerate(directions):

        # Move the robot and record the location it moves to
        if robo_santa and idx % 2 == 0:
            r_loc = move_santa(char, r_loc)
            visted_houses.add(r_loc)

        # Otherwise move Santa and record the location
        else:
            s_loc = move_santa(char, s_loc)
            visted_houses.add(s_loc)

    return len(visted_houses)


def move_santa(char: str, loc: (int, int)) -> (int, int):
    """
    Move a Santa or Robot Santa based on a direction string.
    """
    if char == "^":
        loc = (loc[0], loc[1] + 1)
    elif char == "v":
        loc = (loc[0], loc[1] - 1)
    elif char == ">":
        loc = (loc[0] + 1, loc[1])
    elif char == "<":
        loc = (loc[0] - 1, loc[1])
    else:
        raise Exception(f"Unknown movement char: {char}!")

    return loc


if __name__ == "__main__":
    directions = read_directions("./data/input.txt")
    print(f"Solution to part 1 = {houses_covered(directions)}")
    print(f"Solution to part 2 = {houses_covered(directions, True)}")
