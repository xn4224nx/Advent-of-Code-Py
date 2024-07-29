"""
--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to
submit an order for more. They have a list of the dimensions
(length l, width w, and height h) of each present, and only want
to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular
prism), which makes calculating the required wrapping paper for
each gift a little easier: find the surface area of the box, which
is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper
for each present: the area of the smallest side.

PART 1: All numbers in the elves' list are in feet. How many
        total square feet of wrapping paper should they order?

The elves are also running low on ribbon. Ribbon is all the same
width, so they only have to worry about the length they need to
order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance
around its sides, or the smallest perimeter of any one face. Each
present also requires a bow made out of ribbon as well; the feet
of ribbon required for the perfect bow is equal to the cubic feet
of volume of the present. Don't ask how they tie the bow, though;
they'll never tell.

PART 2: How many total feet of ribbon should they order?
"""

import re


def calc_area(length: int, width: int, height: int) -> int:
    """
    What is the area of wrapping paper required of a certain box?
    This is calculated as the area of the box plus the area of the
    smallest side.
    """
    box_area = 2 * length * width + 2 * width * height + 2 * height * length
    sorted_sides = sorted([length, width, height])
    smallest_side = sorted_sides[0] * sorted_sides[1]

    return box_area + smallest_side


def calc_ribbon(length: int, width: int, height: int) -> int:
    """
    For a box of specific dimensions how much ribbon is also required
    to wrap it?

    Each box need a length of ribbon the same magnitude as the volume for the
    bow. Then is needs a length of ribbon equal to the side with the smallest
    perimeter. The sum of those two values is the total lengths of ribbon
    needed.
    """
    bow_len = length * width * height

    # Find the smallest perimeter of a side
    half_perims = sorted([length + width, width + height, height + length])

    return bow_len + 2 * half_perims[0]


def parse_box_dims(dim_file: str) -> list[(int, int, int)]:
    """
    Read the text file that contains the dimesions of the boxes,
    one per line. And return a list of the sizes.
    [(length, width, height)]
    """

    box_dims = []

    # Read the file into an array of strings
    with open(dim_file) as fp:
        raw_dims = fp.readlines()

    # Cast each list as three integers
    for line in raw_dims:
        l_res = re.search(r"(\d+)x(\d+)x(\d+)", line)
        box_dims.append((int(l_res.group(1)), int(l_res.group(2)), int(l_res.group(3))))

    return box_dims


if __name__ == "__main__":

    total_paper = 0
    total_ribbon = 0

    for length, width, height in parse_box_dims("./data/input.txt"):
        total_paper += calc_area(length, width, height)
        total_ribbon += calc_ribbon(length, width, height)

    print(
        f"The answer to part 1 = {total_paper}\nThe answer to part 2 = {total_ribbon}"
    )
