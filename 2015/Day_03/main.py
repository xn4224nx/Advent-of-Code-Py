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
"""


def read_directions(file_path: str) -> str:
    """
    Open the direction file and return a string of the file
    contents.
    """

    with open(file_path) as fp:
        contents = fp.read().rstrip()

    return contents


def houses_covered(directions: str) -> dict[(int, int), str]:
    """
    Determine the coordinates of houses that are visted by Santa
    when he follows the directions. Return a dict with the
    visted houses and the visit count.
    """
    loc = (0, 0)
    visted_houses = {loc: 1}

    for char in directions:

        if char not in "^>v<":
            continue

        if char == "^":
            loc = (loc[0], loc[1] + 1)
        elif char == "v":
            loc = (loc[0], loc[1] - 1)
        elif char == ">":
            loc = (loc[0] + 1, loc[1])
        elif char == "<":
            loc = (loc[0] - 1, loc[1])

        if loc not in visted_houses:
            visted_houses[loc] = 1
        else:
            visted_houses[loc] += 1

    return visted_houses


if __name__ == "__main__":
    directions = read_directions("./data/input.txt")
    print(f"Solution to part 1 = {len(houses_covered(directions))}")
